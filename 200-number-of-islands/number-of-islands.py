class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        ret = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] =='1' and (i,j) not in visited:
                    ret+=1
                    visited.add((i,j))
                    stack = [(i,j)]
                    while(stack):
                        curr_x,curr_y = stack.pop()
                        adj_list = [(0,1),(1,0),(0,-1),(-1,0)]
                        for x,y in adj_list:
                            a = curr_x+x
                            b = curr_y+y
                            if (a,b) in visited:
                                continue
                            elif (a)>=0 and (a)<m and (b)>=0 and (b)<n and grid[a][b] == '1':
                                visited.add((a,b))
                                stack.append((a,b))

        return ret