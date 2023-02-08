"""
Question Statement
=======================================
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.
=========================================
Time complexity
==========================================
O(n)
Space complexity
==========================================
O(n)
=========================================
Approach
=======================================
Prefix sum
=======================================
"""
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        """
        Initializes the object with the integer matrix matrix.
        """
        if not matrix or not matrix[0]:
            return

        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.prefix_sum = [[0] * (self.col + 1) for _ in range(self.row + 1)]
        
        for i in range(1, self.row + 1):
            for j in range(1, self.col + 1):
                self.prefix_sum[i][j] = self.prefix_sum[i - 1][j] + self.prefix_sum[i][j - 1] - self.prefix_sum[i - 1][j - 1] + matrix[i - 1][j - 1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
        """
        return self.prefix_sum[row2 + 1][col2 + 1] - self.prefix_sum[row2 + 1][col1] - self.prefix_sum[row1][col2 + 1] + self.prefix_sum[row1][col1]
        
