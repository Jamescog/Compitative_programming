"""
Question Statement
================================
Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[0...k-1] (0-indexed).
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3,
  we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

Return an array of the k-values corresponding to a sequence of pancake flips that sort arr.
Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.

Time complexity
========================
O(n^2)
========================
Space complecity
========================
O(n)
========================
Approach
========================
Pancake Sorting
========================
"""
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer = []
        # Iterate through the list from end to start
        for x in range(len(arr), 1, -1):
            # Find the current maximum element 
            current_max = arr.index(x)
            # Add the index of the maximum element and current max value
            answer.extend([current_max + 1, x])

            # Perform flip operation by reversing the subarray
            arr = arr[:current_max:-1] + arr[:current_max]
        
        # Return the list of k-values
        return answer
