class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        amps = [0]*(n+1)
        for i in range(1,len(amps)):
            amps[i] = gain[i-1]+amps[i-1]
        return max(amps)