"""
Question Statement
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
============================
Time complexity
============================
O(n log n)
============================
Space complexity
============================
O(n)
============================
Approach
===========================
Merge sorting
==========================
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # If the length of the input list is greater than 1
        if len(nums) > 1:
            # Find the middle index of the list
            mid = len(nums) // 2
            # Split the input list into left and right halves
            left_half = nums[:mid]
            right_half = nums[mid:]
            # Recursively sort the left and right halves
            self.sortColors(left_half)
            self.sortColors(right_half)
            # Initialize indices for left half, right half, and input list
            i = j = k = 0
            # While there are still elements in both left and right halves
            while i < len(left_half) and j < len(right_half):
                # Compare elements at the current indices in the left and right halves
                if left_half[i] < right_half[j]:
                    # If the element in the left half is smaller, add it to the input list
                    nums[k] = left_half[i]
                    i += 1
                else:
                    # If the element in the right half is smaller, add it to the input list
                    nums[k] = right_half[j]
                    j += 1
                k += 1
            # While there are still elements in the left half
            while i < len(left_half):
                # Add the remaining elements from the left half to the input list
                nums[k] = left_half[i]
                i += 1
                k += 1
            # While there are still elements in the right half
            while j < len(right_half):
                # Add the remaining elements from the right half to the input list
                nums[k] = right_half[j]
                j += 1
                k += 1

