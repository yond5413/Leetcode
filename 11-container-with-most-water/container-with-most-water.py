class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        ret = float("-inf")
        max_l,max_r = height[l],height[r]
        while(l<r):
            if max_l>max_r:
                ret = max(ret,max_r*(r-l))
                r-=1
                max_r = max(max_r,height[r])
                
            else:
                ret = max(ret,max_l*(r-l))
                l+=1
                max_l = max(max_l,height[l])
                
        return ret
