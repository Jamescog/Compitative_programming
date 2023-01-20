"""
Question Statement
====================================================
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.
=====================================================
Time complexity
======================================================
O(n)
======================================================
Space complexity
======================================================
O(1)
======================================================
Approach
======================================================
Two Pointers
======================================================
"""
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                ans += nums[i-1] + 1 - nums[i]
                nums[i] = nums[i-1] + 1
        return ans
