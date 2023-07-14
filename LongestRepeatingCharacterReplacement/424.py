'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
'''
'''
!!!!!!! Solution details !!!!!!!!
- Was kind of tricky brute force nested for loop was not sufficent so attempted sliding door technique 
- initialized an empty dictionary to keep track of char count and used condition (r-l)+1 -freq <= k to see if window was valid 
- freq was the count of the most frequently appearing char in the substring for ex "AAAB" A is the most frequent therefore freq = 3
- if it wasn't valid we would decrement the dictionary and increment the left pointer and continue
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ret = 0
        chars = {}
        l = 0
        freq = 0
        for r in range(0,len(s)):
            if s[r] in chars:
                chars[s[r]] += 1
            else:
                chars[s[r]] = 1
            ################
            # finding most frequent character 
            for i in chars.keys():
                freq = max(chars[i],freq)
            ################
            #print(f"l: {l}, r:{r}, s[l]:{s[l]},s[l]:{s[r]},substr:{s[l:r+1]}")
            #print(chars)
            #print((r-l)-freq)
            if (r-l)+1-freq <=k:
                ret = r-l+1
            else:
                ### increment left pointer 
                chars[s[l]]-= 1
                l+=1 
        return ret
    

        ### another method below I attempted but fails in cases  where first char isn't most frequent     
        '''print(f"len{len(s)}")
        for i in range(0,len(s)-k):
            count = 1
            flag = k
            r = i+1
            cur = s[i]
            while(flag >=0 and r<len(s)):
                print(f"cur:{cur}, i:{i}, r:{r}, flag:{flag}, ret:{ret}")
                if s[r] != s[i]:
                    flag-=1
                cur = cur+s[i]
                r+=1
                if flag>-1:
                    count+=1
            ret =max(ret,count) #max(ret,len(cur))
        ###handles cases well for if it sees left pointer first but another edge cases is 
        #s = "ABBB"
        # @ s[0] we have A and eventually stops at AAA
        # should be BBBB based off test cases
        ## may need how frequently each char appears to handle this issue 
        return ret'''