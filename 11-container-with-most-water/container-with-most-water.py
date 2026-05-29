class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        l_max,r_max = height[l],height[r]
        ret = float("-inf")
        while (l<r):
            if r_max>l_max:
                ret = max(ret,l_max*(r-l))
                l+=1
                l_max = max(height[l],l_max)
            else:
                ret = max(ret,r_max*(r-l))
                r-=1
                r_max = max(height[r],r_max)

        return ret