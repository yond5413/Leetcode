class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n = len(maze),len(maze[0])
        ret = float("inf")
        u,v = entrance
        queue = [(u,v,0)]
        visited = set()
        while queue:
            i,j,steps = queue.pop(0)
            adj = [(1,0),(-1,0),(0,1),(0,-1)]
            if i == 0 or i == m-1 or j == 0 or j == n-1 and maze[i][j] == ".":
                
                ret = min(steps,ret) if [i,j] != entrance else ret
            for x,y in adj:
                d_x,d_y = i+x,j+y
                if d_x>=0 and d_x<m and d_y>=0 and d_y<n:
                    if (d_x,d_y) not in visited and maze[d_x][d_y] == ".":
                        queue.append((d_x,d_y,steps+1))
                        visited.add((d_x,d_y))
            visited.add((i,j))
        return ret if ret != float("inf") else -1