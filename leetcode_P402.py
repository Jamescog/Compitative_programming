"""
Question Statement
=====================================================
Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.
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
Two Pointers
======================================================
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            # while we still have digits to remove and the stack is not empty
            # and the last digit in the stack is greater than the current digit
            while k and stack and stack[-1] > digit:
                stack.pop() # remove the last digit in the stack
                k -= 1
            stack.append(digit) # append the current digit to the stack
        # if we still have digits to remove
        while k:
            stack.pop() # remove the last digit in the stack
            k -= 1
        # remove leading zeroes
        while stack and stack[0] == "0":
            stack.pop(0)
        # if the stack is empty, return "0"
        if not stack:
            return "0"
        # else, return the remaining digits in the stack as a string
        return "".join(stack)
