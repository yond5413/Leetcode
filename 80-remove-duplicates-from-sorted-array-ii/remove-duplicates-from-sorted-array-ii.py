class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        - each entry can appear at most twice
        - still sorted?
        -> sliding window approach
        '''
        '''
        sliding window
        -->we need left pointer(k) to be at least 2 to check l-2
        -> we then check if l-2 is != nums[r] via right pointer so we can overwrite it
        ---> this is because we can have 2 entires in a rowm but we just want to slide valid 
        entries to the left return l as our new length
        '''
        l = 2
        for r in range(2,len(nums)):
            if nums[l-2] != nums[r]:
                nums[l] = nums[r]
                l+=1
        return l