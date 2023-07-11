'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ret = []
        dups = set()
        nums.sort()
        print(nums)
        ##### best approach is doing a 2 pointer approach imo
        ##### done 2sum and 3sum at this point 
        ##### O(n^3)time complexity
        ##### reduce the problem to sorted 2sum from previously 
        #a = 0
        #d = len(nums)-1
        for a in range(0,len(nums)-3):  
            for b in range(a+1,len(nums)-2):
                c=b+1
                d = len(nums)-1
                while(c<d):
                    curr = nums[a] +nums[b] +nums[c] +nums[d]
                    if curr <target:
                        c+=1
                    elif curr> target:
                        d-=1
                    elif curr ==target and tuple([nums[a],nums[b] ,nums[c],nums[d]]) not in dups :
                        ret.append([nums[a],nums[b] ,nums[c],nums[d]])
                        dups.add(tuple([nums[a],nums[b] ,nums[c],nums[d]]))
                        c+=1
                        d-=1
                    else:
                        c+=1
                        d-=1
        return ret 