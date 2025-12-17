class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        stack = []
        ret = ""
        for ch in s:
            if ch.isdigit():
                num = num*10+int(ch)
            elif ch == "[":
                stack.append((ret,num))
                num,ret = 0,""
            elif ch == "]":
                old_str,old_num = stack.pop()
                ret = old_str+ret*old_num
            else:
                ret+=ch
        return ret