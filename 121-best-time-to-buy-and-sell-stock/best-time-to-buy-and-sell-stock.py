class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = float("-inf")
        l = prices[0]
        for i in range(1,len(prices)):
            #print(f"ret:{ret}, curr:{prices[i]-l}")
            ret = max(ret,prices[i]-l)
            
            l  = min(l,prices[i])

        return ret if ret>0 else 0