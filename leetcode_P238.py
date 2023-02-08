"""
Question statement
====================================
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
======================================
Time complexity
=====================================
O(n)
====================================
Space complexity
===================================
O(n)
==================================
Approach
=================================
Prefix sum
================================
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize an array to store the product of elements to the left of each element
        left_product = [1] * n
        # Calculate the product of elements to the left of each element
        for i in range(1, n):
            left_product[i] = left_product[i-1] * nums[i-1]
        
        # Initialize a variable to store the product of elements to the right of each element
        right_product = 1
        # Calculate the product of elements to the right of each element, and update the answer array
        for i in range(n-1, -1, -1):
            left_product[i] *= right_product
            right_product *= nums[i]
        
        return left_product
