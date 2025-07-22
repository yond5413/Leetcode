class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        mini = prices[0]
        for i in range(1,len(prices)):
            if ret< (prices[i]-mini):
                ret = (prices[i]-mini)
            mini = min(prices[i],mini)
        return ret