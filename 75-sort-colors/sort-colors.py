class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0,0,0]
        for i in nums:
            buckets[i]+=1
        i= 0
        for j in range(len(nums)):
            while buckets[i]==0:
                i+=1
            nums[j]=i
            buckets[i] -=1