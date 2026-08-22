class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nums,ret = 0,""
        for ch in s:
            if ch.isdigit():
                nums = nums*10 + int(ch)
            elif ch == "[":
                stack.append((nums,ret))
                nums,ret = 0,""
            elif ch == "]":
                old_nums,old_str = stack.pop(-1)
                ret = old_str + ret*old_nums
            else:
                ret +=ch
        return ret