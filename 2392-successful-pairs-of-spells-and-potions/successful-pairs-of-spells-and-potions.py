class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n,m = len(spells),len(potions)
        ret = []
        potions.sort()
        for i in range(n):
            curr = spells[i]
            l,r = 0,m-1
            while(l<=r):
                j = (r+l)//2
                if curr*potions[j] >=success:
                    r = j-1
                    
                else:
                    l = j+1
            ret.append(m-l)
        return ret
