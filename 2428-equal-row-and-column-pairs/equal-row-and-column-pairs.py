from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ret = 0
        rows = defaultdict(int)
        n = len(grid)
        for i in range(n):
            curr = tuple(grid[i])
            rows[curr] = rows.get(curr,0)+1
        for i in range(n):
            col = [grid[j][i] for j in range(n)]
            ret+= rows.get(tuple(col),0)
        return ret