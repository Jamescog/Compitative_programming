"""
Question statement
========================================
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
==========================================
Time complexity
==========================================
O(n)
==========================================
Space complexity
==========================================
O(n)
==========================================
Approach
==========================================
Stack
==========================================
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize an empty stack to keep track of operands
        stack = []
        for i in tokens:
            # Check if the current token is an operator
            if i in set(['+', '-', '*', '/']):
                # Pop the last two operands from the stack
                a = stack.pop()
                b = stack.pop()
                # Perform the corresponding operation and append the result to the stack
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(b - a)
                elif i == '*':
                    stack.append(a * b)
                else:
                    # handle the division operation
                    stack.append(int(b / a))
            else:
                # if the current token is not an operator, it is an operand, so cast it to int and append to the stack
                stack.append(int(i))
        # The final result is the only element remaining on the stack
        return stack[0]
