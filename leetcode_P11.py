"""
Question Statement
======================================================
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
========================================================
Time complexity
=======================================================
O(n)
=======================================================
Space complexity
=======================================================
O(1)
======================================================
Approach
=====================================================
Two  Pointers
======================================================
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 # initializing left pointer 
        right = len(height) - 1 #initializing right pointer
        max_area = 0 #initializing max_area
        
        # loop until left pointer is less than right pointer
        while left < right:
            curr_area = min(height[left], height[right]) * (right - left) # calculate current area
            max_area = max(max_area, curr_area) # update max area if current area is greater
            
            if height[left] < height[right]:
                left += 1 # if left pointer is shorter, move it towards right
            else:
                right -= 1 # if right pointer is shorter, move it towards left
        
        return max_area # return the max area found
