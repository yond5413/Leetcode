class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount+1
        dp = [float('inf')]*n
        dp[0] = 0
        for i in range(n):
            for c in coins:
                if i-c>=0:
                    dp[i] = min(dp[i],dp[i-c]+1)

        return dp[-1] if dp[-1] != float('inf') else -1