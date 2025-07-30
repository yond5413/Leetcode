class Solution:
    def isNumber(self, s: str) -> bool:
        exp_flag = False
        deci_flag = False
        seen_digit = False
        for i in range(len(s)):
            if (s[i] in ['+','-']):
                if i>0 and s[i-1] not in ['e','E']:
                    return False
            ###############
            elif s[i].isnumeric():
                seen_digit = True
            elif s[i] =='.':
                if exp_flag or deci_flag:
                    return False
                deci_flag = True
            elif s[i] in ['e',"E"]:
                if exp_flag or not seen_digit:
                    return False
                seen_digit = False
                exp_flag = True
            else:
                return False
        return seen_digit