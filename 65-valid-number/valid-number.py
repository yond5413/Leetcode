class Solution:
    def isNumber(self, s: str) -> bool:
        digit = dot = exp = False
        for i in range(len(s)):
            if s[i] in ['+','-']:
                if i>0 and s[i-1] not in ['e','E']:
                    return False
            elif s[i].isnumeric():
                digit = True
            elif s[i] in ['e','E']:
                if not digit or exp:
                    return False
                digit = False
                exp = True
            elif s[i] == '.':
                if dot or exp:
                    return False
                dot = True
            else:
                return False
        return digit