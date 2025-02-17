class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ret = [0]*(2*n-1)
        visited = set()
        def dfs(i: int):
            if i ==len(ret):
                return True
            for num in range(n,0,-1):
                #### boundary/repeats
                if num in visited:
                    continue
                if num>1 and (num+i>=len(ret) or ret[num+i]!=0):
                    continue
                #################
                ret[i] = num
                visited.add(num)
                if num>1:
                    ret[num+i] = num
                # find next val
                j = i
                while (j<len(ret) and ret[j]!=0):
                    j +=1
                if dfs(j):
                    return True
                ret[i] = 0
                visited.remove(num)
                if num>1:
                    ret[num+i] = 0
            return False
                
        dfs(0)
        return ret