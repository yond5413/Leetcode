class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ret = [0]*n
        start = 0
        stack = []
        for log in logs:
            func_id,state,timestamp =log.split(':')
            func_id = int(func_id)
            timestamp = int(timestamp)
            if state == 'start':
                if stack:
                    ret[stack[-1]]+= timestamp - start
                stack.append(func_id)
                start = timestamp
            else:
                ret[stack.pop(-1)]+= timestamp - start+1
                start = timestamp +1

        return ret