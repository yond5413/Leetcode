class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        #max_l,max_r = height[l],height[r]
        ret = 0
        while (l<r):
            if height[r]<height[l]:
                ret = max(ret,height[r]*(r-l))
                r-=1 
            else:
                ret = max(ret,height[l]*(r-l))
                l+=1 
        return ret
        