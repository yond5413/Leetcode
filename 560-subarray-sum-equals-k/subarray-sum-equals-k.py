class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ret = 0
        hashmap = {}
        hashmap[0] = 1
        ## need to populate it 
        curr = 0

        for i in range(len(nums)):
            curr +=nums[i]
            if curr-k in hashmap:
                ret+=hashmap[curr-k]
            hashmap[curr] = 1 if curr not in hashmap else hashmap[curr]+1
            #print(hashmap)
        return ret