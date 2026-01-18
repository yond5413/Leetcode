class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = []
        def dfs(idx,curr,tot):
            if len(curr) ==k and tot == n:
                ret.append(curr[::])
                return 
            for i in range(idx,10):
                if tot+i<=n:
                    dfs(i+1,curr+[i],tot+i)
        dfs(1,[],0)
        return ret