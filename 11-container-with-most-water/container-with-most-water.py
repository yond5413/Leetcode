class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        l_max,r_max = height[l],height[r]
        ret = 0
        while(l<r):
            if l_max<r_max:
                ret = max(ret,(r-l)*l_max)
                l+=1
                l_max = max(l_max,height[l])
            else:
                ret = max(ret,(r-l)*r_max)
                r-=1
                r_max = max(r_max,height[r])
        return ret