class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ret = list()
        hashm = {nums[i]:i for i in range(0,len(nums))}
        #print(hashm)
        ## more optimal use look up table to find targets
        ## i != J
        ## subtract target from curr nums[i] value and check if it is in array then
        ## use look up table to find that index
        for i in range(0,len(nums)):
            match = target - nums[i]
            if match in nums and i != hashm[match]:
                print("match")
                ret.append(i)
                ret.append(hashm[match])
                break
        return ret