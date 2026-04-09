class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        l = 0
        for r in range(len(prices)):
            if prices[l]<=prices[r]:
                ret = max(ret, prices[r]-prices[l])
            else:
                l = r
        return ret