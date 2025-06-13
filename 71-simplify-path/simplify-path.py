class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        stack = []
        for i in s:
            if i == '..':
                if stack: 
                    stack.pop(-1)
            elif i == '' or i == '.':
                pass
            else:
                stack.append(i)
        print(stack)
        ret = '' if stack else '/'
        for i in stack:
            ret = ret + '/'+i
        return ret 