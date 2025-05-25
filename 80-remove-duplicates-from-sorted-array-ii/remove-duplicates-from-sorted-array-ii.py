class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
     
        k = 0
        for i in range(0,len(nums)):
            if k<=1 or nums[k-2] != nums[i]:
                nums[k] = nums[i] 
                k+=1
                
        return k