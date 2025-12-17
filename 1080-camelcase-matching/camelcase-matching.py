class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(query,pattern):
            i,n = 0,len(pattern)
            for ch in query:
                if i<n and ch == pattern[i]:
                    i+=1
                elif ch.isupper():
                    return False
            return i==n
        return [match(q,pattern) for q in queries]