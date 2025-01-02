class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = []
        def dfs(curr,tot,idx):
            if len(curr) == k and tot == n:
                ret.append(curr[:])
                return  
            for i in range(idx,10):
                if tot+i <= n:
                    dfs(curr+[i],tot+i,i+1)
        dfs([],0,1)
        return ret