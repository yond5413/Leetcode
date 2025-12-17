class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ret = 0
        n,m = len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in visited:
                    stack = [(i,j)]
                    ret+=1
                    visited.add((i,j))
                    while (stack):
                        x,y = stack.pop()
                        adj = [(0,1),(1,0),(0,-1),(-1,0)]
                        for a,b in adj:
                            cur_x,cur_y = x+a,y+b
                            if (cur_x,cur_y) in visited:
                                continue
                            elif cur_x>=0 and cur_x<n and cur_y >= 0 and cur_y<m and grid[cur_x][cur_y]=="1":
                                stack.append((cur_x,cur_y))
                                visited.add((cur_x,cur_y))
                        
        return ret