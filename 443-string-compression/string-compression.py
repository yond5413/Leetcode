class Solution:
    def compress(self, chars: List[str]) -> int:
        l,r,n = 0,0,len(chars)
        while r<n:
            curr = chars[r]
            count = 0
            while r<n and curr==chars[r]:
                r+=1
                count+=1
            chars[l] = curr
            l+=1
            if count>1:
                digits = str(count)
                chars[l:l+len(digits)] = digits
                l+= len(digits)
        return l