class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh,rotten = 0,[]
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh +=1
                elif grid[i][j] ==2:
                    rotten.append((i,j))
        queue = [(i,j,1) for i,j in rotten]
        visited = set(rotten)
        ret = 0
        while queue and fresh>0:
            x,y,steps = queue.pop(0)
            ret = max(ret,steps)
            adj = [(0,1),(1,0),(0,-1),(-1,0)]
            for i,j in adj:
                dx,dy = x+i,y+j
                if dx>=0 and dx<m and dy>=0 and dy<n and (dx,dy) not in visited and grid[dx][dy]==1:
                    queue.append((dx,dy,steps+1))
                    visited.add((dx,dy))
                    fresh-=1
        return ret if fresh == 0 else -1

