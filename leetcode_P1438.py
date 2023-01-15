"""
Question statement
=========================================
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that
the absolute difference between any two elements of this subarray is less than or equal to limit.
==========================================
Time complexity
===========================================
O(n)
===========================================
Space complexity
============================================
O(n)
============================================
Approach
===========================================
Deque
============================================
"""
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Initialize two dequeues for keeping track of max and min elements
        maxd = []
        mind = []
        i = 0
        for j in range(len(nums)):
            # Remove elements from maxd that are less than current element
            while maxd and nums[j] > maxd[-1]:
                maxd.pop()
            # Remove elements from mind that are greater than current element
            while mind and nums[j] < mind[-1]:
                mind.pop()
            # Add current element to both maxd and mind
            maxd.append(nums[j])
            mind.append(nums[j])
            # Check if the difference between the current max and min exceeds the limit
            if maxd[0] - mind[0] > limit:
                # If so, remove the element at the start of the dequeues
                if maxd[0] == nums[i]:
                    maxd.pop(0)
                if mind[0] == nums[i]:
                    mind.pop(0)
                i += 1
        # Return the length of the longest subarray
        return j - i + 1
