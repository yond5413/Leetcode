class Solution:
    def decodeString(self, s: str) -> str:
        ret = ""
        stack = []
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)
            elif ch == "[":
                stack.append((ret,num))
                ret,num = '',0
            elif ch == "]":
                old_str,old_num = stack.pop()
                ret = old_str+old_num*ret
            else:
                ret += ch
        return ret