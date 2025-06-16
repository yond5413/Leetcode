class Solution:
    def maximumSwap(self, num: int) -> int:
        num_s = list(str(num))
        n = len(num_s)
        max_r = [0]*n
        max_r[n-1] = n-1
        # 1st Pass
        for i in range(n-2,-1,-1):
            max_r[i] = i if int(num_s[i]) > int(num_s[max_r[i+1]]) else max_r[i+1]
        # 2nd Pass
        for i in range(n):
            if int(num_s[i])< int(num_s[max_r[i]]):
                num_s[i],num_s[max_r[i]] = num_s[max_r[i]],num_s[i]
                return int(''.join(num_s))
        return num