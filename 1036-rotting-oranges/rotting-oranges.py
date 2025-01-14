class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ret,fresh = 0,0
        rows, cols = len(grid),len(grid[0])
        queue = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c)) 
                elif grid[r][c] ==1:
                    fresh +=1
        ############################
        # bfs now
        while(queue and fresh>0):
            for i in range(len(queue)):
                x,y = queue.pop(0)
                adj = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
                for i,j in adj:
                    if i>r or i<0 or j>c or j<0:
                        continue
                    if grid[i][j] == 1:
                        grid[i][j] =2 
                        queue.append((i,j))
                        fresh -=1

            ret+=1


        return ret if fresh ==0 else -1