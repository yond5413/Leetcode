class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == k:
            return max(nums)
        freq = [0]*51
        for i in nums:
            freq[i]+=1
        if k == 1:
            for i in range(50,-1,-1):
                if freq[i] ==1:
                    return i
            return -1
        ret = -1
        if freq[nums[0]] ==1:
            ret =  max(ret,nums[0])
        if freq[nums[-1]] ==1:
            ret = max(ret,nums[-1])
        return ret