"""
Question statement
=================================================
Given two integer arrays pushed and popped each with distinct values,
return true if this could have been the result of a sequence of push and pop operations on an initially empty stack,
or false otherwise.
===============================================
Time complexity
================================================
O(n)
================================================
Space complexity
================================================
O(n)
=================================================
Approach
=================================================
Iterative Approach
================================================
"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = [] # Create a stack
        j = 0 # Intialise one pointer pointing on popped array
    
        for val in pushed:
            st.append(val) # insert the values in stack
            while len(st) != 0 and st[-1] == popped[j]: # if st.peek() values equal to popped[j];
                st.pop() # then pop out
                j += 1 # increment j
    
        return len(st) == 0 # check if stack is empty
