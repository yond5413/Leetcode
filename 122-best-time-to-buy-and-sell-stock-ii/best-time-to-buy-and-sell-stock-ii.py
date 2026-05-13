class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        n = len(prices)
        def dfs (idx,buy):
            if idx == n:
                return 0
            if (idx,buy) in dp:
                return dp[(idx,buy)]
            hold = dfs(idx+1,buy)
            if buy:
                profit = -prices[idx]+dfs(idx+1,not buy) 
            else:
                profit = prices[idx] + dfs(idx+1,not buy) 
            dp[(idx,buy)] = max(profit,hold)
            return dp[(idx,buy)]
        return dfs(0,True)