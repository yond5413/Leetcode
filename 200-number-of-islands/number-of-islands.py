class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        visited = set()
        ret =0
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == "1":
                    ret+=1
                    queue = [(i,j)]
                    visited.add((i,j))
                    while queue:
                        x,y = queue.pop(0)
                        adj = [(0,1),(1,0),(0,-1),(-1,0)]
                        for u,v in adj:
                            dx,dy = x+u,y+v
                            if dx>=0 and dx<m and dy>=0 and dy<n and grid[dx][dy]== "1":
                                if (dx,dy) not in visited:
                                    visited.add((dx,dy))
                                    queue.append((dx,dy))
        return ret
