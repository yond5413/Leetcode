'''
Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 '''
class Solution(object):
    def twoSum(self,nums,target):
            ret = list()
            for i in range(0,len(nums)):
                for j in range(i+1,len(nums)):
                    sum = nums[i]+nums[j]
                    if sum == target:
                        ret.append(i)
                        ret.append(j)
            return ret