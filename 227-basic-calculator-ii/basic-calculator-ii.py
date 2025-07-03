class Solution:
    def calculate(self, s: str) -> int:
        ## MDAS
        ret=prev=curr = 0
        curr_opp = '+'
        i=0
        while(i<len(s)):
            curr_char = s[i]
            if curr_char.isdigit():
                while i<len(s) and s[i].isdigit():
                    curr = curr*10 + int(s[i])
                    i+=1
                i-=1
                if curr_opp == '+':
                    ret +=curr
                    prev = curr
                elif curr_opp == '-':
                    ret -= curr
                    prev = -curr
                elif curr_opp == '*':
                    ret-=prev
                    ret += prev*curr
                    prev = prev*curr
                elif curr_opp == '/':
                    ret -= prev
                    ret+= int(prev/curr)#prev//curr
                    prev = int(prev/curr)#prev//curr
                curr = 0
            elif curr_char != ' ':
                curr_opp = curr_char
            i+=1
        return ret