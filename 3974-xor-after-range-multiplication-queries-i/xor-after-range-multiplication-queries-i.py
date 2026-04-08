class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        
        #q[i] = [l_i,r_i,k_i,v_i]
        #idx = l_i
        #nums[idx] = (nums[idx]*v_i)
        #idx +=k_i
        n = len(nums)
        for i in range(len(queries)):
            idx = queries[i][0]
            r = queries[i][1]
            k = queries[i][2]
            v = queries[i][3]
            while(idx<=r):
                nums[idx] = (nums[idx]*v)%(7+10**9)
                idx+=k
        ret = 0
        for val in nums:
            ret^=val
        return ret

