class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ret = float("inf")
        u,v = entrance
        m,n = len(maze),len(maze[0])
        queue = [(u,v,0)]
        visit = set()
        while queue:
            i,j,steps = queue.pop(0)
            if maze[i][j] == "+":
                continue
            if  i == 0 or i == m-1 or j == 0 or j == n-1 :  
                ret = min(ret,steps) if [i,j] != entrance else ret
            adj = [(1,0),(-1,0),(0,1),(0,-1)]
            visit.add((i,j))
            for x,y in adj:
                dx,dy = i+x,j+y
                if dx >=0 and dx <m and dy>=0 and dy<n and maze[dx][dy] == ".":
                    if (dx,dy) not in visit:
                        queue.append((dx,dy,steps+1))
                        visit.add((dx,dy))
        return ret if ret != float("inf") else -1