"""
Question Statement
===============================================
You are given an array people where people[i] is the weight of the ith person,
and an infinite number of boats where each boat can carry a maximum weight of limit.
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
==============================================
Time complexity
===============================================
O(n)
===============================================
Space complexity
===============================================
O(1)
===============================================
Approach
===============================================
Two-pointers
===============================================
"""
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # sort the people by their weight
        i, j = 0, len(people) - 1 # two pointers, one from start and one from end
        count = 0 # to keep track of number of boats needed
        while i <= j:
            if people[i] + people[j] <= limit: # if the current two people's weight is within limit
                i += 1 # move the start pointer to right
            j -= 1 # move the end pointer to left, since we can use the heavier person in any case
            count += 1 # increment the number of boats used
        return count
