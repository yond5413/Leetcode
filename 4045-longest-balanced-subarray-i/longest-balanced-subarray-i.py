class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)
        for i in range(n):
            even,odd = set(),set()
            for j in range(i,n):
                if nums[j]%2 ==1:
                    odd.add(nums[j])
                else:
                    even.add(nums[j])
                if len(even) == len(odd):
                    ret = max(j-i+1,ret)
        return ret

