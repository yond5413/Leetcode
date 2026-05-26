class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lookup = set(word)
        special = set()
        for s in word:
            if s.lower() in lookup and s.upper() in lookup:
                special.add(s.lower())
        return len(special)