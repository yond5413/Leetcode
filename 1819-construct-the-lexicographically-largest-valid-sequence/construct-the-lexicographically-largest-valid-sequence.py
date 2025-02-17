class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2*n-1
        ret = [0]*size
        # integer 1 occurs once
        # every integer between 2 and n occurs twice
        # for every integer i between 2 and n, the distance
        ## between the 2 occurences of i is exactly i.
        visited = set()
        def dfs(idx: int):
            if len(ret) == idx:
                return True
            for num in range(n,0,-1):
                # seen before 
                if num in visited:
                    continue
                # out of bounds 
                if num>1 and (num+idx >= len(ret) or ret[num+idx] !=0):
                    continue 
                ###############
                visited.add(num)
                ret[idx] = num
                if num>1:
                    ret[num+idx] = num
                #############################
                # find next step
                j = idx+1
                while(j<len(ret) and ret[j] !=0):
                    j+=1
                #################################
                if dfs(j):
                    return True
                ########backtrack######
                visited.remove(num)
                ret[idx] =0
                if num>1:
                    ret[num+idx] = 0
            return False
        dfs(0)
        return ret
