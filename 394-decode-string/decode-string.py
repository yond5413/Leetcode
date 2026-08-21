class Solution:
    def decodeString(self, s: str) -> str:
        num, ret = 0,""
        stack = []
        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)
            elif ch == "[":
                stack.append((num,ret))
                num, ret = 0,""
            elif ch == "]":
                old_num,old_str = stack.pop(-1)
                ret = old_str + ret*old_num     
            else:
                ret+= ch           
        return ret