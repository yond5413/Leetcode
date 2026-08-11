class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_cand = max(candies)
        n = len(candies)
        ret = [False]*n
        for i in range(n):
            if max_cand <= candies[i]+extraCandies:
                ret[i] = True
        return ret