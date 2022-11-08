'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''

class Solution:
    def reverse(self, x: int) -> int:
        ############################
        bit32 = (2**31) - 1
        negBit32 = -1*(2**31)
        ret = 0
        
        flag = 0
    ### check if it is negative
        if x < flag:
            flag = -1 
        xStr = str(x)
        xReverseStr = xStr[::-1]## flipped str version of x
        
        intStorage = 0
        if flag == -1:
            xReverseStr = xReverseStr[:len(xReverseStr) -1]
            # removes - sign at the end so I can convert back to int
            intStorage =int(xReverseStr)*flag
        else:
            intStorage = intStorage =int(xReverseStr)
          
        if intStorage <= bit32 and intStorage >=negBit32:
            ret = intStorage

        return ret 