class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        hashmap = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
        }
        ret = []
        def dfs(cur,idx):
            if idx == len(digits):
                ret.append(''.join(cur[:]))
                return 
            chars = hashmap[digits[idx]]
            for i in chars:
                cur.append(i)
                dfs(cur,idx+1)
                cur.pop()
        dfs([],0)
        return ret
