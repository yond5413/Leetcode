class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ret = 0
        n = len(gain)
        prefix = [0]*(n+1)
        for i in range(1,n+1):
            prefix[i] = gain[i-1]+prefix[i-1]
        print(prefix)
        ret = max(prefix)
        return ret
