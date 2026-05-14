class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        print(n)
        # base[n] = [1,2,3...n-1,n,n]
        if len(nums) != n+1:
            return False
        freq = Counter(nums)
        for i in range(1,n+1):
            if i not in freq:
                return False
            if i == n:
                if freq[n]<2:
                    return False
        return True

