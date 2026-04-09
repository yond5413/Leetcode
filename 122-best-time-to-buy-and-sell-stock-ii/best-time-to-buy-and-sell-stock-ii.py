class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lookup = {}
        def dfs(idx,buy):
            if idx == len(prices):
                return 0
            if (idx,buy) in lookup:
                return lookup[(idx,buy)]
            hold = dfs(idx+1, buy) ## 
            if buy:
                profit = dfs(idx+1,not buy)-prices[idx]
            else:
                profit = profit = dfs(idx+1,not buy)+prices[idx]
            lookup[(idx,buy)] = max(profit,hold)
            return lookup[(idx,buy)]
        return dfs(0,True)
        