"""
Question Statement
=====================================
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
=====================================
Time complexity
=====================================
O(n)
=====================================
Space complexity
=====================================
O(1)
=====================================
Approach
=====================================
Cyclic replacement
=====================================
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n # to handle k > n
        count = 0 # to keep track of number of elements rotated
        for start in range(n):
            current = start
            prev = nums[start]
            while count < n:
                next_index = (current + k) % n
                nums[next_index], prev = prev, nums[next_index]
                current = next_index
                count += 1
                if current == start: # if we have completed a cycle
                    break
