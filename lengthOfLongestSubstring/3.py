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
#### done with 2 pointer technique not optimal really still basically operating like a nested loop in O(n^2) time complexity
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)<1):
            return 0
        ret = 1
        for i in range(0,len(s)):
            j =i+1
            count = 1
            while(j!=len(s)):
                curr = s[i:j]
                if s[j] in curr:
                    break
                else:
                    count+=1
                j+=1
            ret = max(count,ret)
        return ret