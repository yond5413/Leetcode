class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lookup = {}
        n = len(prices)
        def dfs(buy,idx):
            if idx == n:
                return 0
            if (buy,idx) in lookup:
                return lookup[(buy,idx)]
            hold = dfs(buy,idx+1)
            if buy:
                profit = -prices[idx] + dfs(not buy,idx+1)
            else:
                profit = prices[idx] + dfs(not buy, idx+1)
            lookup[(buy,idx)] = max(profit,hold)
            return lookup[(buy,idx)]
        return dfs(True,0)
            