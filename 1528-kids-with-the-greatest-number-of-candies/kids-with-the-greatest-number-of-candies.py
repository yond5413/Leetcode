class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        ret = [False]*n
        max_cand = max(candies)
        for i in range(n):
            if candies[i]+extraCandies >=max_cand:
                ret[i] = True
        return ret