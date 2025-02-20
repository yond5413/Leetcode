class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        lookup = []
        visited =set() #set(nums)
        #print(visited)
        def dfs(curr: str):
            if len(curr) == n and curr not in visited:
                lookup.append(curr)
                visited.add(curr)
                return 
            for i in ['0','1']:
                if (curr+i) not in visited:
                    #visited.add(curr+i)
                    dfs(curr+i) 
                    #visited.remove(curr+i)
        dfs('')
        for i in range(len(lookup)):
            if lookup[i] not in nums:
                return lookup[i]
        return ''
