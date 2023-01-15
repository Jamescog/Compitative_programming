"""
Question Statement
=====================================================
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.
====================================================
Time complexity
====================================================
O(n)
=====================================================
Space complexity
======================================================
O(n)
======================================================
Approach
======================================================
Stack
======================================================
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n # create a list with the same size as temperatures and fill with 0 
        stack = [] # initialize a monostack
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]: # check if the current temperature is greater than
              # the temperature at the top of the stack
                j = stack.pop() # if it is, pop the top of the stack
                res[j] = i - j # the number of days to wait for a warmer temperature is the current index minus the popped index
            stack.append(i) # push the current index onto the stack
        return res
