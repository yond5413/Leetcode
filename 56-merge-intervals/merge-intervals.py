class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =lambda x: x[0])
        ret = []
        curr = intervals[0]
        
        for i in range(1,len(intervals)):
            if curr[1]>=intervals[i][0]:
                curr[1] = intervals[i][1] if intervals[i][1]>curr[1] else curr[1]
            else:
                ret.append(curr)
                curr = intervals[i]
        ret.append(curr)
        
        return ret 