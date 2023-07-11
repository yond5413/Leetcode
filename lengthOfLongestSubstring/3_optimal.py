'''
Given a string s, find the length of the longest substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)<1):
            return 0
        ret = 1
        dup = set()
        ###########
        # sliding window technique 
        ''' Summary 
        Essentially we seet our sub array at index 0 and loop through array with out right pointer(r)
        we check if there is a duplicate in the while loop and update our left pointer(l) accordingly
        We then update the set at end of the for loop by adding the current s[r] to the set
        ret = max(ret,r-l+1) comes from finding length of substring and picking the largest of the two values
        '''
        l = 0
        for r in range(0,len(s)):
            while(s[r] in dup):
                dup.remove(s[l])
                l+=1
            dup.add(s[r])
            ret = max(ret,abs(l-r)+1)
        return ret