class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        visited = set()
        rotten,fresh =[],0 
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==1:
                    fresh+=1
                elif grid[i][j] ==2:
                    rotten.append((i,j))
        queue = [(r,j,1) for r,j in rotten]
        visited = set(rotten)
        while (queue and fresh):
            x,y,t = queue.pop(0)        
            adj = [(1,0),(0,1),(-1,0),(0,-1)]
            for u,v in adj:
                dx,dy = x+u, y+v
                if dx>=0 and dx<m and dy>=0 and dy<n and grid[dx][dy] ==1:
                    if (dx,dy) not in visited:
                        visited.add((dx,dy))
                        queue.append((dx,dy,t+1))
                        fresh-=1
            ret = max(ret,t)
        return ret if fresh == 0 else -1
