"""
Question statement
=====================================
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
====================================
Time complexity
===================================
O(n)
===================================
Space complexity
===================================
O(n)
===================================
Approach
==================================
Prefix sum
==================================
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1} # initialize prefix_sum dictionary with 0:1
        sum = 0
        count = 0
        for num in nums:
            sum += num
            if sum - k in prefix_sum:
                count += prefix_sum[sum - k]
            prefix_sum[sum] = prefix_sum.get(sum, 0) + 1
        return count
