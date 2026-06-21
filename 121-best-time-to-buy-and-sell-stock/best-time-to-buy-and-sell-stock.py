class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        l = prices[0]
        for r in range(1,len(prices)):
            print(f"l: {l}, prices[r]: {prices[r]}")
            ret = max(ret,prices[r]-l)
            l = min(prices[r],l)
        
        return ret if ret !=float("-inf") else 0 