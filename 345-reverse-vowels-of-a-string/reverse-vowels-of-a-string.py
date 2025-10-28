class Solution:
    def reverseVowels(self, s: str) -> str:
        curr = list(s)
        l,r = 0,len(s)-1
        vowels = ["a","e","i",'o',"u","A","E","I","O","U"]
        vowels = set(vowels)
        while l<=r:
            if curr[l] in vowels and curr[r] in vowels:
                temp = s[l]
                curr[l] = curr[r]
                curr[r] = temp
                l+=1
                r-=1
            elif curr[l] in vowels and curr[r] not in vowels:
                r-=1
            elif curr[l] not in vowels and curr[r] in vowels:
                l+=1
            else:
                r-=1
                l+=1
        return "".join(curr)