class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        lookup = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }
        visited = set()
        n = len(digits)
        def dfs(idx,curr):
            if idx == n:
                visited.add(curr)
                ret.append(curr[::])
                return
            paths = lookup[digits[idx]]
            for p in paths:
                if curr+p not in visited:
                    visited.add(curr+p)
                    dfs(idx+1,curr+p)
        dfs(0,"")
        return ret