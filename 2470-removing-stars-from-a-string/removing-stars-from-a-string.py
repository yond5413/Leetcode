class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "*":
                if stack:
                    stack.pop(-1)
            else:
                stack.append(ch)
        return "".join(stack)
            