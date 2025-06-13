class Solution:
    def simplifyPath(self, path: str) -> str:
        easy = path.split('/') 
        print(easy)
        stack = []
        for s in easy:
                if s == "":
                    pass
                elif s == '.':
                    pass
                elif s== '..':
                    if stack:
                        stack.pop(-1)
                else:
                    stack.append(s)
        ret = ''
        for s in stack:
            ret = ret+'/'+s 
        return ret if ret !='' else '/'