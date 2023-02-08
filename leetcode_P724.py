"""
Question statement
======================================
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
===================================
Time complexity
===================================
O(n)
===================================
Space complexity
===================================
O(1)
===================================
Approach
===================================
Prefix sum
===================================
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Calculate the total sum of the array
        total_sum = sum(nums)
            # Initialize left_sum as 0
        left_sum = 0
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Subtract the current number from the total sum to get the right sum
            right_sum = total_sum - left_sum - num
            
            # If left_sum and right_sum are equal, return the current index
            if left_sum == right_sum:
                return i
            
            # Increment left_sum by the current number
            left_sum += num
        
        # Return -1 if no such index exists
        return -1
