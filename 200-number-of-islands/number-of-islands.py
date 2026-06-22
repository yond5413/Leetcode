class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        visited = set()
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if  grid[i][j] == "1" and (i,j) not in visited:
                    ret+=1
                    visited.add((i,j))
                    queue = [(i,j)]
                    adj = [(0,1),(1,0),(0,-1),(-1,0)]
                    while queue:
                        x,y = queue.pop(0)
                        for a,b in adj:
                            dx,dy = x+a,y+b
                            if dx>=0 and dx<m and dy>=0 and dy<n and grid[dx][dy] == "1" and (dx,dy) not in visited:
                                visited.add((dx,dy))
                                queue.append((dx,dy))

        return ret