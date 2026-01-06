class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        u,v = entrance
        m,n = len(maze),len(maze[0])
        visit = set()
        queue = [(u,v,0)]
        ret = float("inf")
        while queue:
            i,j,steps = queue.pop(0)
            if maze[i][j] == "+":
                continue
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                ret = min(ret,steps) if [i,j] !=entrance else ret
            adj = [(1,0),(-1,0),(0,1),(0,-1)]
            for x,y in adj:
                d_x,d_y = i+x,j+y
                if d_x>=0 and d_x<m and d_y>=0 and d_y<n:
                    if (d_x,d_y) not in visit and maze[d_x][d_y] == ".":
                        queue.append((d_x,d_y,steps+1))
                        visit.add((d_x,d_y))
            visit.add((i,j))

        return ret if ret != float("inf") else -1