class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        lookup = []
        visited =set(nums)
        #print(visited)
        def dfs(curr: str):
            if len(curr) == n and curr not in visited:
                lookup.append(curr)
                visited.add(curr)
                return lookup[-1]
            for i in ['0','1']:
                if (curr+i) not in visited:
                    #visited.add(curr+i)
                    dfs(curr+i) 
                    if lookup:
                        return lookup[-1]
                    #visited.remove(curr+i)
            return 
        dfs('')
        return '' if not lookup else lookup[0]
        