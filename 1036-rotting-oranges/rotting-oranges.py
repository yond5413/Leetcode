class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ret = 0
        fresh = 0
        m,n  = len(grid),len(grid[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j,1))
                elif grid[i][j] ==1:
                    fresh+=1
        #######################################
        while (queue and fresh>0):
            i,j,step = queue.pop(0)
            adj = [(1,0),(-1,0),(0,1),(0,-1)]
            for x,y in adj:
                dx,dy = x+i,y+j
                if dx>=0 and dx<m and dy>=0 and dy<n:
                    if grid[dx][dy] ==1:
                        fresh-=1
                        queue.append((dx,dy,step+1))
                        grid[dx][dy] = 2
            ret = max(step,ret)
        return ret if fresh == 0 else -1
