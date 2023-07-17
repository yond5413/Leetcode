'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
#### Solution notes
'''
solved using a stack 
we use our dictionary/hashmap to check if it is an opening or closing char
if opening add to stack
if closing check if top of stack (end of str/list in this) is the matching char 
repeat until done or a fail condition occurs
-
'''
class Solution:
    def isValid(self, s: str) -> bool:
        #ret = True
        check = {')':'(', '}':'{', ']':'['}
        stack = []
        for i in s:
            #print(f"len(stack):{len(stack)}, curr:{i}, stack{stack}")
            ### opening condtion
            if i not in check:
                stack.append(i)
                continue
            #### closing condition####
            if len(stack) == 0 or check[i] !=stack[-1]:
                #print("fail condition")
                #print(f"len(stack):{len(stack)}, curr:{i}, stack{stack}")
                ret = False
                return ret
            stack.pop()
        #print("end")
        #print(f"len(stack):{len(stack)}, stack{stack}")
        return len(stack) == 0
    
        