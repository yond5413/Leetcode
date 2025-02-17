from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        hashmap = Counter(tiles)
        #print(hashmap)
        visited = set()
        def dfs(curr: str):
            for k in list(hashmap.keys()):
                if hashmap[k]>0 and (curr+k) not in visited:
                    visited.add(curr+k)
                    hashmap[k]-=1
                    dfs(curr+k)
                    hashmap[k]+=1
        dfs('')    
        return len(visited)

