class Solution:
    def getTop(self,stack: list, part: str):
        return ''.join(stack)[len(stack)-len(part):] == part

    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n= len(part)
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack)>=n and self.getTop(stack,part):
                for _ in range(n):
                    stack.pop(-1)
            
        return ''.join(stack)