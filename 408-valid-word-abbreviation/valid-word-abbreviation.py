class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # can replace substring with length of it
        # no leading zeroes in abbr
        # cannot be adjacent as it can be confusing
        i,j = 0,0
        m,n = len(abbr),len(word)
        while(j<m and i<n):
            #print(f"i:{i},j:{j}")
            if abbr[j].isdigit():
                offset = 0
                if abbr[j] =='0':
                    return False
                while(j<m and abbr[j].isdigit()):
                    offset= offset*10+int(abbr[j])
                    j+=1
                if i+offset<=n:
                    i+=offset
                else:
                    #print('TRUST')
                    return False
            elif abbr[j]!=word[i]:
                #print('LMAO')
                return False
            else:
                i+=1
                j+=1
        return True if i ==n and j == m else False
        