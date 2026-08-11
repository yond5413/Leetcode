class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a","e","i","o","u"])
        new_s = list(s)
        l,r = 0, len(new_s)-1
        while (l<r):
            v_l = new_s[l].lower() in vowels
            v_r = new_s[r].lower() in vowels
            if v_l and v_r:
                new_s[l],new_s[r] = new_s[r],new_s[l]
                l+=1
                r-=1
            elif v_l:
                r-=1
            elif v_r:
                l+=1
            else:
                l+=1
                r-=1
        return ("").join(new_s)