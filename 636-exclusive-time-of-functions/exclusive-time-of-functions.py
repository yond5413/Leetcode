class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ret= [0]*n
        prev_start_time = 0
        stack = []
        for log in logs:
            func_id,state,timestamp = log.split(":")
            func_id = int(func_id)
            timestamp = int(timestamp)
            if state == 'start':
                if stack:
                    ret[stack[-1]]+=timestamp - prev_start_time
                stack.append(func_id)
                prev_start_time = timestamp
            else:
                ret[stack.pop(-1)]+= timestamp - prev_start_time+1
                prev_start_time = timestamp +1
        return ret