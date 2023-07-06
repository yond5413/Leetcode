'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = "".join(i for i in s if i.isalnum())#isalphanum())
        ### filters non letters
        ## could just use ord to access ascii 
        l = 0
        r = len(newS)-1
        print(newS)
        while(l<r):
            if newS[l].lower() == newS[r].lower():
                l+=1
                r-=1
                print(f"l: {l}, r{r}, newS[l]:{newS[l]}, newS[r]:{newS[r]}")
            else:
                return False
        return True
        