/*
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
*/


class Solution {
    public int lengthOfLongestSubstring(String s) {
        /////////////// simple cases///////////////
        if(s == null){
            return 0;
        }
        if(s.length() < 2){
            return s.length();
        }
        ////////////////////////////////////////////
        int ret = 1;
        StringBuilder temp =new StringBuilder().append(s.charAt(0));
        char[] chars = s.toCharArray(); 
        /////////////////////////////////////////////////////////////
        for(int i = 1; i< chars.length; i++){
        String t = String.valueOf(chars[i]);
        String string = temp.toString();
            temp.append(t);
            if(string.contains(t)){
                string = temp.toString().substring(string.indexOf(t)+1);
                temp = new StringBuilder(string);
            }
            
            else{
                ret = Math.max(ret, temp.toString().length());    
            }
            
        }
        
        return ret;
    }
}