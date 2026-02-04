from typing import List
import math

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        NEG_INF = float('-inf')  # safe -inf for constraint given

        # DP arrays
        inc1 = [NEG_INF] * n
        dec  = [NEG_INF] * n
        inc2 = [NEG_INF] * n

        ans = NEG_INF

        for i in range(1, n):
            # increasing
            if nums[i-1] < nums[i]:
                inc1[i] = max(inc1[i-1] + nums[i], nums[i-1] + nums[i])

            # Phase 2: decreasing 
            if nums[i-1] > nums[i]:
                dec[i] = max(dec[i-1] + nums[i], inc1[i-1] + nums[i])

            # Phase 3: increasing again 
            if nums[i-1] < nums[i]:
                inc2[i] = max(inc2[i-1] + nums[i], dec[i-1] + nums[i])
                ans = max(ans, inc2[i])

        return ans if ans != NEG_INF else -1