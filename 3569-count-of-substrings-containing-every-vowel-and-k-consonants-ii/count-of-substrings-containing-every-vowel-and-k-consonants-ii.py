from collections import defaultdict
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def helper(k):
            vowel = defaultdict(int)
            nonvowel = 0
            l = 0
            ret = 0
            for r in range(len(word)):
                if word[r] in 'aeiou':
                    vowel[word[r]]+=1
                else:
                    nonvowel+=1
                #################
                while(len(vowel)==5 and nonvowel>=k):
                    ret +=len(word)-r
                    if word[l] in 'aeiou':
                        vowel[word[l]]-=1
                    else:
                        nonvowel-=1
                    if vowel[word[l]] ==0:
                        vowel.pop(word[l])
                    l+=1
            return ret
        return helper(k)-helper(k+1)