class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        l_max,r_max = height[l],height[r]
        ret = 0
        while(l<r):
            if l_max<=r_max:
                ret += max(0,(l_max-height[l]))    
                l+=1
                l_max = max(height[l],l_max)
            else:
                ret += max(0,(r_max-height[r]))     
                r-=1
                r_max = max(height[r],r_max)

        return ret