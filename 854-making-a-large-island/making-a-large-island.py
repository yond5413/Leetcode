class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        lookup = {}
        n = len(grid)
        visited = set()
        label = 2
        adj = [(1,0),(0,1),(-1,0),(0,-1)]
        def is_valid(r,c):
            return r>=0 and r<n and c>=0 and c<n
        #####################################
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    queue = [(i,j)]
                    count = 0
                    while (queue):
                        x,y = queue.pop()
                        grid[x][y] = label
                        for a,b in adj:
                            if is_valid(x+a,y+b) and (x+a,y+b) not in visited and grid[x+a][y+b]==1:
                                queue.append((x+a,y+b))
                                visited.add((x+a,y+b))
                        count+=1
                    lookup[label] = count
                    label+=1
        print(lookup)
        def connect(r,c):
            ret = 1
            new_visited = set()
            for i,j in adj:
                if is_valid(r+i,c+j) and grid[r+i][c+j] not in new_visited and grid[r+i][j+c] in lookup:
                    ret+=lookup[grid[r+i][c+j]]
                    new_visited.add(grid[r+i][c+j])
            return ret

        ret = 0 if not lookup else max(lookup.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    ret = max(ret,connect(i,j))
        return ret
            



