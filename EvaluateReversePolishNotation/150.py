'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 
Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 
Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
'''
##########
'''
Solution Notes
-Given the nature of the input using a stack to keep track of numeric variables made this problem a lot simpler
-Essentially just check to see if it is a numerical value and push to stack if it is a operator pop the top to values from the stack 
then append result of operation
'''
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ret = 0
        operands = "+-/*"       
        numeric = list()
        for i in tokens:
            if i not in operands:
                numeric.append(int(i))
            else:
                ### should be at least list len>=2
                a = numeric.pop()
                b = numeric.pop()
                print(f"a:{a} {i} b:{b}")  
                if i == "+":
                    print(f"res: {a+b}")
                    numeric.append(a+b)
                elif i == "-":
                    print(f"res: {a-b}")
                    numeric.append(b-a)
                elif i == "/":
                    print(f"res: {int(b/a)}")
                    numeric.append(int(b/a))
                elif i == "*":
                    print(f"res: {a*b}")
                    numeric.append(a*b)
        ret = numeric[0] 
        return ret
        