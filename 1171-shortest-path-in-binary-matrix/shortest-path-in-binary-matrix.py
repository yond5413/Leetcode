class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = [(0,0,1)]
        visited = set()
        adj_list = [(1,0),(0,1),(1,1),(-1,-1),
        (-1,0),(0,-1),(1,-1),(-1,1)]
        while queue:
            i,j,steps = queue.pop(0)
            if min(i,j)<0 or max(i,j)>=n or grid[i][j]:
                continue
            if i == n-1 and j == n-1:
                return steps
            for x,y in adj_list:
                if (x+i,y+j) not in visited:
                    queue.append((x+i,y+j,steps+1)) 
                    visited.add((x+i,y+j))
        return -1