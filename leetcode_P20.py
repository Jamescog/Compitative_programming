"""
Question statement
===============================
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
================================
Time complexity
=================================
O(n)
=================================
Space complexity
=================================
O(n)
=================================
Approach
=================================
Stack
=================================
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # Create matching dictionary
        matching = {"}":"{", ")":"(", "]":"["}
        # Create stack to keep track of the openning bracket
        stack = []

        # Do the checking
        for char in s:
            if char in matching.values():
                stack.append(char)
            elif stack and matching[char] == stack[-1]:
                stack.pop()
            else:
                return False
        # Return True is the stack is empty.
        return stack == []
