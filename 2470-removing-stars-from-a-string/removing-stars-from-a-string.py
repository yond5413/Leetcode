class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        ret = ''
        for ch in s:
            if ch == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        for ch in stack:
            ret+=ch
        return ret