class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = [(entrance[0],entrance[1],0)]
        ret = -1
        m,n = len(maze),len(maze[0])
        visited = set()
        while(queue):
            x,y,steps = queue.pop(0)
            adj = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            if (x,y) in visited:
                continue
            if x == 0 or y == 0 or x == m-1 or y == n-1:
                if [x,y] != entrance:
                    return steps
            visited.add((x,y))
            for i,j in adj:
                if i<0 or i>=m or j<0 or j>=n:
                    continue
                if (i,j) not in visited and maze[i][j] != '+':
                    queue.append((i,j,steps+1)) 
        return ret