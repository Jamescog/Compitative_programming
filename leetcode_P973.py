"""
Question Statement
==============================
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
===============================
Time complexity
===============================
O(n log n)
===============================
Space complexity
===============================
O(n)
===============================
Approach
===============================
Sorting
===============================
"""
class Solution:
    from math import sqrt
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #  Points with distances
        points_with_distance = [(point, sqrt(point[0]**2 + point[1]**2)) for point in points]
        # Sort the points based on the distance
        points_with_distance.sort(key=lambda x:x[1])

        # Return the k points 
        return [point[0] for point in points_with_distance[:k]]
