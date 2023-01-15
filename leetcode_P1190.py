"""
Question statement
======================================================================
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.
=========================================================================
Time complexity
=========================================================================
O(n)
=========================================================================
Space complexity
=========================================================================
O(n)
=========================================================================
Approach
=========================================================================
Two-Pointer
=========================================================================
"""
class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Create an empty list to store the indices of opening parentheses
        opened = []
        # Create a dictionary to store the corresponding indices of opening and closing parentheses
        pair = {}
        
        # Iterate through the input string
        for i in range(len(s)):
            # If the current character is an opening parenthesis, add its index to the list
            if s[i] == '(':
                opened.append(i)
            # If the current character is a closing parenthesis,
            # store its corresponding opening parenthesis index in the dictionary
            if s[i] == ')':
                j = opened.pop()
                pair[i] = j
                pair[j] = i
        
        # Initialize the result string
        res = ""
        # Set the starting index and direction for iteration
        i = 0
        d = 1
        # Iterate through the input string
        while i < len(s):
            # If the current character is an opening or closing parenthesis,
            # update the current index and change the direction of iteration
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                d = -d
            # Otherwise, append the current character to the result string
            else:
                res += s[i]
            i += d
        
        # Return the modified result string
        return res
