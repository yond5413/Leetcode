''' 
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer =[1]*len(nums) #[]
        ## init
        prefix = [1]*len(nums)#list()
        postfix = [1]*len(nums)#list()
        pre_store = 1
        post_store = 1
        ### getting prefix and postfix values 
        for i in range(len(nums)):
            prefix[i] *= nums[i]*pre_store
            pre_store *=nums[i]   
            #print("here: "+str( prefix[i]))
            postfix[-(i+1)] *= post_store*nums[-(i+1)]
            post_store *=nums[-(i+1)]
        #print("###########")
        #print("prefix: "+str(prefix))
        #print("postfix: "+str(postfix))
        ### manipulate arrays to get correct values in answer list()
        for i in range(len(nums)):
            pre = 0
            post = 0
            if (i-1) < 0:
                pre = 1
            else:
                pre = prefix[i-1]
            if (i) == len(nums)-1:
                post = 1
            else:
                post = postfix[i+1]
            answer[i] = pre*post
            #print("pre: "+str(pre))
            #print("post: "+str(post))   
        return answer 
ans = Solution()
print(ans.productExceptSelf([1,2,3,4]))