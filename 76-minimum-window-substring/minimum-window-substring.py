class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or len(s)<len(t):
            return ''
        l = 0
        s_map,t_map = {},{}
        m,n = len(s),len(t)
        for i in range(n):
            if t[i] not in t_map:
                t_map[t[i]] = 1
                s_map[t[i]] = 0
            else:
                t_map[t[i]] += 1
        ##################################
        have,need = 0,len(t_map)
        res,count = [-1,-1],float("inf")
        for r in range(m):
            s_map[s[r]] = s_map.get(s[r],0)+1
            if s[r] in t_map and s_map[s[r]] ==t_map[s[r]]:
                have+=1
            while(have == need):
                if (r-l) +1 < count:
                    res = [l,r]
                    count = (r-l) +1
                s_map[s[l]] -=1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    have -=1
                l+=1
        l,r = res
        print(f"l:{l},r:{r}")
        return s[l:r+1] if count != float('inf') else ''