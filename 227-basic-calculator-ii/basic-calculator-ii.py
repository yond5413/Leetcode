class Solution:
    def calculate(self, s: str) -> int:
        prev= curr = ret = 0
        i = 0
        curr_op = '+'
        while i<len(s):
            curr_char  =s[i]
            if curr_char.isdigit():
                while i<len(s) and s[i].isdigit():
                    curr = curr*10 + int(s[i])
                    i+=1
                i-=1
                if curr_op =='+':
                    ret +=curr
                    prev = curr
                elif curr_op =='-':
                    ret -=curr
                    prev = -curr
                elif curr_op =='*':
                    ret -=prev
                    ret += prev*curr
                    prev =  prev*curr
                elif curr_op =='/':
                    ret -=prev
                    ret += int(prev/curr)
                    prev = int(prev/curr)
                curr = 0
            elif curr_char != ' ':
                curr_op = s[i]
            i+=1

        return ret
