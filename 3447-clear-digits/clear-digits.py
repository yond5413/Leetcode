class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        ret = ""
        for i in range(len(s)):
            if s[i].isnumeric():
                if stack:
                    stack.pop()
                else:
                    print('stack is empty???')
            else:
                stack.append(s[i])
        while(stack):
            ret+= stack.pop()
        return ret[::-1]