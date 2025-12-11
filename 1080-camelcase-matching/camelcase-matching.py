class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(query,pattern):
            n = len(pattern)
            p = 0
            for c in query:
                if p<n and pattern[p] ==c:
                    p+=1
                elif c.isupper():
                    return False
            return p==n
        ##########################
        return [match(q,pattern) for q in queries]
