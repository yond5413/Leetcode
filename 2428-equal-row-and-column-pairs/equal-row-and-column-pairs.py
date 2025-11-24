class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ret = 0
        n = len(grid)
        rows = {}
        for i in range(n):
            curr = tuple(grid[i]) ## Lists are not hashable
            rows[curr] = 1+rows.get(curr,0)
        for i in range(n):
            cols = [grid[j][i] for j in range(n)]
            ret += rows.get(tuple(cols),0)

        return ret