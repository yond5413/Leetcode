class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        fails = set()
        for i in range(len(s)):
            if s[i] not in "()":
                continue
            elif s[i] == '(':
                stack.append(i)
            elif not stack:
                fails.add(i)
            else:
                stack.pop()
        ret = ''
        for i in stack:
            fails.add(i)
        for i in range(len(s)):
            if i not in fails:
                ret+=s[i]
        return ret