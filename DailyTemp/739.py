'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''
####### Solution notes
'''
-Took me a but of time to kind of understand tbh but essentially to solve this I used a stack 
-initially tried sliding window but it was to slow for leetcode
- Essentially we use a monolithic stack (decreasing) order->LIFO
- as we iterate through each day we hceck if the current days is larger than the top of the stack and if it is we pop that value until
empty or we find a day with a larger temp then we append the current day to top of stack.
- the stack stores tuples fo temperatures and index/current day
'''

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ret = [0]*len(temperatures)
        stack = list() ## tuple(val,index)
        i = 0
        for i in range(0,len(temperatures)):
            curr = tuple([temperatures[i],i])
            while(len(stack)>=1 and curr[0]>stack[-1][0]):
                holder = stack.pop(-1)
                ret[holder[1]] = i-holder[1]
            stack.append(curr)
        return ret 