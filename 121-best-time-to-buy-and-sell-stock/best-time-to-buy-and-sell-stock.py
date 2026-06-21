class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        l = prices[0]
        for i in range(1,len(prices)):
            ret = max(prices[i]-l,ret)
            l = min(l,prices[i])
        return ret