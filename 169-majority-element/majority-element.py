class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ret = 0
        visited = {}
        for i in range(len(nums)):
            if nums[i] not in visited:
                visited[nums[i]] = 1
            else:
                visited[nums[i]] += 1
        n = len(nums)
        for k in list(visited.keys()):
            if visited[k] > n//2:
                ret = k
                return ret