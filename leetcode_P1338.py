"""
Question statement
=============================
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.
=============================
Time complexity
=============================
=============================
Space complexity
=============================
=============================
Approach
=============================
============================
"""
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        count = {}

        # Count the occurance of each element
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        count = list(count.values())
        count.sort(reverse=True)

        sum_count = 0


        for i in range(len(count)):
            sum_count += count[i]
            if sum_count >= n/2:
                return i + 1
