"""
Question statement 
==============================
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
====================================================
Time complexity
================================
O(log3(n))
================================
 Space complexity
 ===============================
 O(1)
 ===============================
 Approach
 ===============================
 Two Pointers
 ===============================
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        left, right = 0, 20
        
        while left <= right:
            mid = (left + right) // 2
            num = 3 ** mid
            if num == n:
                return True
            elif num < n:
                left = mid + 1
            else:
                right = mid - 1
        return False