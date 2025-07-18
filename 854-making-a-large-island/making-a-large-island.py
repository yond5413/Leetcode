class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        lookup = {}
        label = 2
        visited = set()
        n  =len(grid)
        adj = [(0,1),(1,0),(0,-1),(-1,0)]
        def is_valid(r,c):
            return r>=0 and r<n and c>=0 and c<n
        for i in range(n):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] ==1:
                    queue = [(i,j)]
                    count = 0
                    visited.add((i,j))
                    while queue:
                        x,y = queue.pop(0)
                        grid[x][y] = label
                        for a,b in adj:
                            if (x+a,y+b) not in visited and is_valid(x+a,y+b) and grid[x+a][y+b] ==1:
                                queue.append((x+a,y+b))
                                visited.add((x+a,y+b))

                        count +=1
                    lookup[label] = count
                    label+=1
        def connect(r,c):
            ret =1
            new_set = set()
            for x,y in adj:
                if is_valid(x+r,y+c) and grid[x+r][y+c] not in new_set and grid[x+r][y+c]>1:
                    ret +=lookup[grid[x+r][y+c]]
                    new_set.add(grid[x+r][y+c])
            return ret
        ret = 0 if not lookup else max(lookup.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    ret = max(ret,connect(i,j))
        return ret
