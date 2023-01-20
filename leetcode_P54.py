"""
Question statement
=================================================
Given an m x n matrix, return all elements of the matrix in spiral order.
=================================================
Time complexity
================================================
O(n)
=================================================
Space complexity
================================================
O(n)
================================================
Approach
================================================
Two Pointers
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Two pointers approach
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1
        ans = []

        while left <= right and top <= bottom:
            # Traverse from left to right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # Traverse from right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # Traverse from bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans
