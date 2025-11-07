class Solution:
    def compress(self, chars: List[str]) -> int:
        l,r = 0,0
        while r<len(chars):
            curr = chars[r]
            count = 0
            while r<len(chars) and curr ==chars[r]:
                r+=1
                count+=1
            chars[l] = curr
            l+=1
            if count>1:
                digits = str(count)
                chars[l:l+len(digits)] = list(digits)
                l+=len(digits)
        return l