class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        digit = 0
        ret = ""
        for ch in s:
            if ch.isdigit():
                digit = digit*10 + int(ch)
            elif ch =="[":
                stack.append((digit,ret))
                digit = 0
                ret = ""
            elif ch =="]":
                old_num,old_str = stack.pop(-1)
                ret = old_str + ret*old_num
            else:
                ret +=ch
        return ret
