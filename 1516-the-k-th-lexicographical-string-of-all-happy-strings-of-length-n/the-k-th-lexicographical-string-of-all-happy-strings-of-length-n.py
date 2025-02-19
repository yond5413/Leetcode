class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        storage = []
        visited = set()
        def dfs(curr):
            if len(curr) == n:
                storage.append(curr)
                return 
            choices = ['a', 'b', 'c']
            visited.add(curr)
            for ch in choices:
                if len(curr)>0 and curr[-1] ==ch:
                    continue
                dfs(curr+ch)
        dfs('')
        print(storage)
        return '' if len(storage)<k else storage[k-1]