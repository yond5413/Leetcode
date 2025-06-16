class Solution:
    def maximumSwap(self, num: int) -> int:
        '''
        Ideally skip 9's
        1 swap to get max num
        '''
        str_num = list(str(num))
        n = len(str_num)
        max_r = [0]*n
        max_r[n-1] = n-1 ## stores idx
        ######################
        ## 2 passes to compute
        # first -> find index of largest value from right
        for i in range(n-2,-1,-1):
            max_r[i] = i if int(str_num[i])>int(str_num[max_r[i+1]]) else max_r[i+1]
        # second
        for i in range(n):
            if int(str_num[i]) < int(str_num[max_r[i]]):
                str_num[i],str_num[max_r[i]]=str_num[max_r[i]], str_num[i]  
                return int(''.join(str_num))

        return num # no swap