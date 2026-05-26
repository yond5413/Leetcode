class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        ret = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == 1:
                    queue = [(i,j)]
                    visited.add((i,j))
                    curr = 1
                    while queue:
                        x,y = queue.pop(0)
                        adj = [(1,0),(0,1),(-1,0),(0,-1)]
                        for u,v in adj:
                            dx,dy = x+u,y+v
                            if dx>=0 and dx<m and dy<n and dy>=0 and grid[dx][dy] == 1:
                                if (dx,dy) not in visited:
                                    curr +=1
                                    visited.add((dx,dy))
                                    queue.append((dx,dy))
                        ret = max(ret,curr)

        return ret