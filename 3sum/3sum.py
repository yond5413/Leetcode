'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ret = []
        nums.sort()
        #print(nums)
        l,r = 0,len(nums)-1
        curr = 0
        dups = set()
        #### sliding window 
        ## use left and right pointer and iterate between the 
        #flag = 0
        #while(l<r):
        for i in range(0,len(nums)-2):
            l = i+1
            r = len(nums)-1
            print(f"before while with i: {i} and nums[i]:{nums[i]}")
            while(r-l>0):
                curr = nums[i] + nums[l] + nums[r]
                #print(f"curr: {curr}, nums[l]:{nums[l]}, nums[r]:{nums[r]}")
                if curr>0:
                    r-=1
                elif curr<0:
                    l+=1
                elif curr == 0 and (nums[i],nums[l],nums[r]) not in dups:
                    ret.append([nums[i],nums[l],nums[r]])
                    dups.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                else:
                    l+=1 
                    r-=1
        return ret