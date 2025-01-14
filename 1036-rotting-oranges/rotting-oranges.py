class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ret,fresh = 0,0
        m,n = len(grid),len(grid[0])
        queue = list()
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh +=1
        while(queue and fresh >0):
            for _ in range(len(queue)):
                x,y = queue.pop(0)
                adj = [(1,0),(-1,0),(0,-1),(0,1)]
                for i,j in adj:
                    dx,dy = x+i,y+j
                    if dx>=m or dx<0 or dy>=n or dy<0:
                        continue
                    print(f"{(dx,dy)}, {(m,n)}")
                    if grid[dx][dy] == 1:
                        fresh-=1
                        grid[dx][dy] =2 
                        queue.append((dx,dy))
            ret +=1
        return ret if fresh == 0 else -1