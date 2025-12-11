class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(query,pattern):
            n = len(pattern)
            i = 0
            for c in query:
                if i<n and c == pattern[i]:
                    i+=1
                elif c.isupper():
                    return False
            return i == n
        return [match(q,pattern) for q in queries]