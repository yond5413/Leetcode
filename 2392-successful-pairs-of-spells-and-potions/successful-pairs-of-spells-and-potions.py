class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ret = []
        n,m = len(spells),len(potions)
        potions.sort()
        for i in range(n):
            l,r = 0,m-1
            while(l<=r):
                j = (r+l)//2
                if spells[i]*potions[j]>=success:
                    r = j-1
                else:
                    l = j+1
            ret.append(m-l)
        return ret