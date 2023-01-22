"""
Question statement 
==============================
Given a string s which represents an expression,
evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid.
All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function
which evaluates strings as mathematical expressions,
such as eval().
====================================================
Time complexity
================================
O(n)
================================
 Space complexity
 ===============================
 O(1)
 ===============================
 Approach
 ===============================
 MiniStack
 ===============================
"""
class Solution:
    def calculate(self, s: str) -> int:
        # Initialize variables
        current = 0
        previous = 0
        result = 0
        operator = "+"
        
        # Iterate through the string
        while current < len(s):
            # Skip whitespace
            while current < len(s) and s[current].isspace():
                current += 1
            
            # Get the next number
            num = 0
            while current < len(s) and s[current].isdigit():
                num = num * 10 + int(s[current])
                current += 1
            
            # Perform the appropriate operation based on the previous operator
            if operator == "+":
                result += previous
                previous = num
            elif operator == "-":
                result += previous
                previous = -num
            elif operator == "*":
                previous *= num
            elif operator == "/":
                previous = int(previous / num)  # Truncate towards zero
            
            # Get the next operator
            if current < len(s):
                operator = s[current]
                current += 1
        
        # Add the final previous number to the result
        result += previous
        
        return result