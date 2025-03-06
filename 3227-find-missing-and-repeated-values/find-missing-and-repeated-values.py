class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n  = len(grid)
        hashmap = {}
        
        ## find num counts in grid
        for i in range(n):
            for j in range(n):
                if grid[i][j] in hashmap:
                    hashmap[grid[i][j]] +=1
                else: 
                    hashmap[grid[i][j]] = 1
        repeat,missing = [],[]
        for i in range(1,n*n+1):
            if i not in hashmap:
                missing.append(i)
            elif hashmap[i]>1:
                repeat.append(i)
        return repeat+missing
