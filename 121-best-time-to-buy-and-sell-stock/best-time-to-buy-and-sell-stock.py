class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = float("-inf")
        n = len(prices)
        future = [0]*n
        future[-1] = prices[-1]
        for i in range(n-2,-1,-1):
            future[i] = max(future[i+1],prices[i])
        #print(future)
        for i in range(n):
            #print(f"ret:{ret}, foo:{future[i]-prices[i]}")
            ret = max(ret,future[i]-prices[i])
            #print(ret)
        return ret