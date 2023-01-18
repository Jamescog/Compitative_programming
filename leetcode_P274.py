"""
Question Statement
=========================================
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.
==========================================
Time complexity
==========================================
O(log(n))
==========================================
Space complexity
==========================================
O(1)
==========================================
Approach
=========================================
Two Pointers
=========================================
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()  # Sort the array of citations in non-decreasing order
        left, right = 0, len(citations)-1  # Initialize two pointers, left and right
        h_index = 0  # Initialize variable to store h_index
        
        # Iterate until left pointer is less than or equal to right pointer
        while left <= right:
            mid = (left + right) // 2  # calculate the middle index
            if citations[mid] >= len(citations) - mid:
                h_index = len(citations) - mid  # Update h_index if current index satisfies the condition
                right = mid - 1  # Move the right pointer towards left
            else:
                left = mid + 1  # Move the left pointer towards right
        return h_index  # Return the h-index

 
