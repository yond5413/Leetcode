class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if not words:
            return []
        ret = [words[0]]
        n = len(words)
        curr = groups[0]
        for i in range(1,n):
            if curr != groups[i]:
                ret.append(words[i])
                curr = groups[i]
        return ret

