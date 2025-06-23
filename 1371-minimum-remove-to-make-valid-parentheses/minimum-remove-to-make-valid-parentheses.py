class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        fail = set()
        for i in range(len(s)):
            if s[i] not in "()":
                continue
            elif s[i] == '(':
                stack.append(i)
            elif not stack:
                fail.add(i)
            else:
                stack.pop()
                
        for i in stack:
            fail.add(i)
        ret = ''
        for i in range(len(s)):
            if i not in fail:
                ret+=s[i]
        return ret