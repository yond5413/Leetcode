class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        ret = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] =='1':
                    ret+=1
                    queue = [(i,j)]
                    visited[i][j] = True
                    while(queue):
                        curr_x,curr_y = queue.pop(0)
                        adj_list = [(curr_x+1,curr_y),(curr_x-1,curr_y),(curr_x,curr_y+1),(curr_x,curr_y-1)]
                        for x,y in adj_list:
                            if x>=0 and x<m and y>=0 and y<n:
                                if not visited[x][y] and grid[x][y] == '1':
                                    queue.append((x,y))
                                    visited[x][y] = True
        return ret