class Solution:
    def tribonacci(self, n: int) -> int:
        seq = [0,1,1]
        
        for i in range(3,n+3):
            seq.append(seq[i-1]+seq[i-2]+seq[i-3])
        return seq[n]