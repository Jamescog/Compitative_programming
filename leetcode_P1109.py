"""
Question statement
=======================================
There are n flights that are labeled from 1 to n.

You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.

Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.
=========================================
Time complexity
==========================================
O(n)
==========================================
Space complexity
=========================================
O(n)
=========================================
Approach
=========================================
Prefix sum
=========================================
"""
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # Create an array to store the seat reservation count for each flight
        seats = [0] * (n + 1)
        
        # Iterate through each booking and update the seats count
        for i, j, k in bookings:
            seats[i - 1] += k
            seats[j] -= k
        
        # Use prefix sum approach to get the cumulative sum of seats
        for i in range(1, n):
            seats[i] += seats[i - 1]
        
        # Return the number of seats reserved for each flight
        return seats[:n]
