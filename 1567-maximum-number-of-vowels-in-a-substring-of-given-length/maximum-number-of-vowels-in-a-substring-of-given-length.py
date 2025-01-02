class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        hashmap = {'a':0,'e':0,'i':0,'o':0,'u':0}
        l = 0
        curr = 0
        for r in range(k):
            if s[r] in hashmap:
                hashmap[s[r].lower()]+=1
                curr +=1
        
        ret = curr
        n = len(s)
        for r in range(k,n):
            if s[r] in hashmap:
                hashmap[s[r].lower()] +=1
                curr +=1
            if s[l] in hashmap:
                hashmap[s[l].lower()] -=1
                curr -=1
            l+=1
            ret = max(ret,curr)
        return ret

    