'''
Given an integer num, return three consecutive integers (as a sorted array) that sum to num. If num cannot be expressed as the sum of three consecutive integers, return an empty array.

Example 1:

Input: num = 33
Output: [10,11,12]
Explanation: 33 can be expressed as 10 + 11 + 12 = 33.
10, 11, 12 are 3 consecutive integers, so we return [10, 11, 12].
Example 2:

Input: num = 4
Output: []
Explanation: There is no way to express 4 as the sum of 3 consecutive integers.
'''
'''
#### Solution Notes ####
- Essentially this problem is asking is num divisble by 3 
- We can then have 3 consective numbers by having an array with the quotient, quotient-1 and quotient +1 
to get the output we are looking for
'''
class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        ret = []
        if num%3 == 0:
            div = num//3
            ret.append(div-1)
            ret.append(div)
            ret.append(div+1)
        return ret