'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ret = list()
        '''
        iterate over input, sort, store letters in dictionary/hashmap
        '''
        #unique= set() ## stores string should be in alphabetical order
        storage = {} ## key/value -> ordered string/[of each anagram]
        for i in range(0,len(strs)):
            if not(str(sorted(strs[i])) in storage):
                storage[str(sorted(strs[i]))] = [strs[i]]
            else:
                list_holder = storage[str(sorted(strs[i]))]
                list_holder.append(strs[i])
                storage[str(sorted(strs[i]))] = list_holder
        for i in storage.values():
            ret.append(i)
        return ret
sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))