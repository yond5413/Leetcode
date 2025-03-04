class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        '''
        distinct powers of 3
        max is 3^16 through hint1

        '''
        powers = [3**i for i in range(17)]
        visited = set()
        def backtrack(curr,idx):
            if curr == n:
                return True
            for i in range(idx,len(powers)):
                if powers[i] not in visited and n:
                    visited.add(powers[i])
                    if backtrack(curr+powers[i],i):
                        return True
                    visited.remove(powers[i])
            return False
        return backtrack(0,0)
