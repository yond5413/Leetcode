'''Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ret = 0
        setNum = set(nums)
        #lengths = list()
        for i in range(0,len(nums)):
            ## check if left is in set to find beginning of sequence
            ## check if nums to continue 
            if (nums[i]-1) not in setNum:
                length = 1 
                while(nums[i]+length in setNum):
                    length+=1
                ret = max(ret,length)
        return ret 