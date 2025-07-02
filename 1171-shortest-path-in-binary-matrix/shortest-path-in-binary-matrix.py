class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = [(0,0,1)]
        visited = set()
        adj_list = [(0,1),(1,0),(1,1),(-1,-1),
        (-1,0),(0,-1),(-1,1),(1,-1)]
        while queue:
            r,c,steps = queue.pop(0)
            if min(r,c)<0 or max(r,c)>=n or grid[r][c]:
                continue
            if r ==n-1 and c==n-1:
                return steps
            for i,j in adj_list:
                if (r+i,c+j) not in visited:
                    queue.append((r+i,c+j,steps+1))
                    visited.add((r+i,c+j)) 
        return -1