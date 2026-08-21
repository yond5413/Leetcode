class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i != "*":
                stack.append(i)
            elif i == "*" and stack:
                stack.pop(-1)
        return "".join(stack)