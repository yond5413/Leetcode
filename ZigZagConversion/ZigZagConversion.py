'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000

solution info 

'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ###### Empty/Trivial case########
        if len(s) <2 or s == "" or s == None or numRows == 1:
            return s
        #################################

        ret = ""
        rows = list()
        for i in range(0,numRows):
            rows.append("")
        flag = 0
        rowCount = 0
        for i in range(0,len(s)):
            rows[rowCount]  = rows[rowCount] + s[i]
            ##handles increasing rows or down the zigzag
            if flag == 0 and rowCount < (numRows-1):
                rowCount +=1
            elif  flag == 0 and rowCount <=(numRows-1):
                rowCount -=1
                flag = 1
            #############################################
            ##handles decreasing rows or going up the zigzag
            elif flag == 1 and rowCount > 0:
                rowCount -=1
            elif  flag == 1 and rowCount == 0:
                rowCount +=1
                flag = 0
        for i in range(0,len(rows)):
            print("row "+str(i)+" =" +rows[i])
            ret = ret + rows[i] #mistyped ret+=blah and it was causing issues
        return ret
