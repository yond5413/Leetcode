class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        curr = n
        while curr not in visited:
            visited.add(curr)
            s =str(curr)
            curr =sum(int(i)**2 for i in s )
            if curr ==1:
                return True
        return False