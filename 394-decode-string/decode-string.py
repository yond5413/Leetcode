class Solution:
    def decodeString(self, s: str) -> str:
        ret = ''
        digit = 0
        stack = []
        for ch in s:
            if ch.isdigit():
                digit = digit*10 + int(ch)
            elif ch == "[":
                stack.append((digit,ret))
                ret = ""
                digit = 0
            elif ch == "]":
                old_num,old_str = stack.pop(-1)
                ret = old_str + ret*old_num
                '''
                Essentially old_str is done already we are just pushing, so update doesn't touch it
                end bracket (]) shows it is time to decompress current str
                '''
            else:
                ret +=ch
        return ret
