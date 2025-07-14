class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ret = []
        max_h,r = heights[n-1],n-1
        ret.append(r)
        for l in range(r-1,-1,-1):
            if max_h<heights[l]:
                ret.append(l)
                max_h = heights[l]
                r = l
        ret = ret[::-1]
        return ret