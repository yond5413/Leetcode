class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        simp = path.split('/')
        for i in simp:
            if i == '':
                pass
            elif i == '.':
                pass
            elif i == '..':
                if stack:
                    stack.pop(-1)
            else:
                stack.append(i)
        ret = ''
        for i in stack:
            ret = ret+'/'+i
        
        return ret if len(ret)!=0 else '/'