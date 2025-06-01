class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i,buy):
            if i == len(prices):
                return 0
            if (i,buy) in dp:
                return dp[(i,buy)]
            hold = dfs(i+1,buy)
            if buy:
                profit = dfs(i+1,not buy) - prices[i]
            else:
                profit = dfs(i+1,not buy) + prices[i]
            dp[(i,buy)] = max(profit,hold)
            return dp[(i,buy)]
        return dfs(0,True)