class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]=1+freq[nums[i]]
            else:
                freq[nums[i]]=1
        ret = None
        print(freq)
        for i in range(len(nums)):
            if not ret or freq[ret] <=freq[nums[i]]:
                ret = nums[i]
        return ret
