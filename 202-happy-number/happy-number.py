class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        curr = n
        while curr not in visit:
            temp = str(curr)
            visit.add(curr)
            curr = sum(int(i)**2 for i in temp)
            if curr == 1:
                return True
        return False
