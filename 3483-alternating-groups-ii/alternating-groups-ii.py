class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        '''
        -> first and last are connected
        ''' 
        n = len(colors)
        l= 0
        ret = 0
        for r in range(1,n+k-1):
            if colors[r%n] == colors[r%n-1]:
                l = r
                # reset window
                # mod to handle circular array
            if r-l+1 >k:
                l+=1
            if r-l+1 == k:
                ret+=1
                
            #######
        return ret
