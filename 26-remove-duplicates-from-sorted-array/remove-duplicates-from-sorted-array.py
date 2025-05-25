class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if i ==0 or nums[i-1] == nums[i]:
                k = k+1 if i==0 else k
                continue
            nums[k] = nums[i]
            k+=1
            #print(f"nums:{nums}, k:{k},i:{i}")
        return k