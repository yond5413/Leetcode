class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l= 0
        curr = 0
        ret = float('inf')
        for r in range(len(blocks)):
            if blocks[r] == 'W':
                curr+=1
            if (r-l)+1 == k:
                ret = min(ret,curr)
                if blocks[l]=='W':
                    curr-=1
                l+=1
        return ret