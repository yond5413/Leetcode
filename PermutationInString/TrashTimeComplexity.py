'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''

'''
!!!!!!!!!!Solution Summary!!!!!!!!!!!!
-Using a hashmap we kept track of the counts of each char in s1
-then we used a sliding window technique to reduce time complexity
-if we found a match that was of the same length as s1 we compared the counts of each char to cover all possible permutations of 
input s1
- initial conditions were to handle cases where s2<s1 and when len(s1) ==1
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) <= len(s2):
            smaller = s1
            larger = s2
            if len(s1) ==1 and s1 in s2:
                return True
            elif len(s1) ==1 and s1 in s2: 
                return False
        else:
            return False 
        ret = False
        count_s = {}
        count_l = {}
        ######################
        for i in smaller:
            if i in count_s:
                count_s[i]+=1
            else:
                count_s[i] =1
        l = 0       
        #######################
        for r in range(0,len(larger)):
            #print(f"l:{l}, r:{r}, larger: {larger[l:r+1]}")
            if larger[r] in count_s:
                count_l[larger[r]] = 1+count_l.get(larger[r],0)
                if len(larger[l:r+1]) == len(smaller):
                    smallSet = set(smaller)
                    for i in smallSet:
                        if count_l.get(i,0) == count_s.get(i,0) and i in larger[l:r+1]:#if count_l[i] == count_s[i]:
                            ret = True
                            #print(f'larger: {larger[l:r+1]} vs smaller: {s1}')
                            #print(f"count_l:{count_l}, count_s: {count_s}")
                        else:
                            #print("Fail condition")
                            #print(f"smallset: {smallSet}")
                            #print(f"count_l:{count_l}, count_s: {count_s}")
                            ret = False
                            if larger[l] in count_l: 
                                count_l[larger[l]] -=1
                            l+=1
                            break
                    if ret == True:
                        return ret
            else:
                #reset count
                #print("reset condition")
                #print(f"count_l:{count_l}")
                count_l= {}
                l=r#l+=1
        return ret