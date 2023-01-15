"""
Question statement
==========================================================================
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.
==============================================================================
Time complexity
==============================================================================
O(n)
==============================================================================
Space complexity
===============================================================================
O(n)
===============================================================================
Approach
==============================================================================
Sliding Window
"""
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)  # number of elements in the array
        ans = n+1  # initialize the minimum length of the subarray as one more than the length of the array
        # create a list to keep track of the running sum of the elements in the array
        prefix_sum = [0]*n
        prefix_sum[0] = nums[0]
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        # create a deque to keep track of the subarray with the smallest sum that is greater than or equal to k
        Pre = deque()
        for i in range(n):
            if prefix_sum[i] >= k:  # if the current sum is greater than or equal to k
                ans = min(ans,i+1)  # update the minimum length of the subarray
            
            while Pre and prefix_sum[i] - prefix_sum[Pre[0]] >= k:
                # if the difference between the current sum and the sum of the subarray at the front of the deque is greater than or equal to k
                ans = min(ans,i-Pre.popleft())  # update the minimum length of the subarray

            while Pre and prefix_sum[Pre[-1]] >= prefix_sum[i]:
                # if the sum of the subarray at the back of the deque is greater than or equal to the current sum
                Pre.pop()  # remove it from the deque
            
            Pre.append(i)  # add the current index to the deque
        
        return -1 if ans == n+1 else ans  # return -1 if no subarray is found, otherwise return the minimum length
