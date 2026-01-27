class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        lookup = {}
        def helper(idx,buy):
            if idx>=len(prices):
                return 0
            if (idx,buy) in lookup:
                return lookup[(idx,buy)]
            cooldown = helper(idx+1,buy)
            if buy:
                bought = helper(idx+1,not buy) - prices[idx]
                lookup[(idx,buy)] = max(bought,cooldown)
            if not buy:
                sell = helper(idx+1,not buy) + prices[idx] - fee
                lookup[(idx,buy)] = max(sell,cooldown)
            return lookup[(idx,buy)]
        ret = helper(0,True)
        return ret
    

