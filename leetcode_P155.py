"""
Question statement 
==============================
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
====================================================
Time complexity
================================
O(1)
================================
 Space complexity
 ===============================
 O(n)
 ===============================
 Approach
 ===============================
 MiniStack
 ===============================
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        """
        Push a value onto the stack and also pushes it onto the min_stack if it is less than or equal to the current minimum.
        """
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        """
        Remove the top value from the stack and also removes it from the min_stack if it is the current minimum.
        """
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self) -> int:
        """
        Return the top value on the stack
        """
        if self.stack:
            return self.stack[-1]
    
    def getMin(self) -> int:
        """
        Return the current minimum value in the stack
        """
        if self.min_stack:
            return self.min_stack[-1]
