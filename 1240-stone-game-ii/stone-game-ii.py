class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp ={}
        def dfs(alice,i,M):
            if i == len(piles):
                return 0
            if (alice,i,M) in dp:
                return dp[(alice,i,M)]
            ret = 0 if alice else float("inf")
            tot = 0
            for X in range(1,2*M+1):
                if X+i>len(piles):
                    break
                tot += piles[i+X-1]
                if alice:
                    ret = max(ret,tot+dfs(not alice, i+X,max(M,X)))
                else:
                    ret = min(ret,dfs(not alice, i+X,max(M,X)))
            dp[(alice,i,M)] = ret
            return ret
        return dfs(True,0,1)