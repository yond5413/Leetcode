class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ret = 0
        n = len(grid)
        rows = {}

        for i in range(n):
            curr_row = tuple(grid[i])
            rows[curr_row] = 1 + rows.get(curr_row,0)
        for i in range(n):
            col = [grid[j][i] for j in range(n)]
            ret += rows.get(tuple(col),0)
        return ret