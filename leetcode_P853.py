"""
Question Statement
==============================================================
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.
===============================================================
Time complexity
================================================================
O(n)
================================================================
Space complexity
===============================================================
O(n)
==============================================================
Approach
===============================================================
Simple Iteration
==============================================================
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            dist = target - position[i] #distance between destination and current car position
            time = dist/speed[i]  #time it takes for the car to reach the destination
            cars.append((position[i],time))
        cars.sort(key = lambda x: x[0]) #sort the cars by their position
        cars.reverse() #reverse the order of cars so that the one which is closest to the destination is at the first
        st = []
        for i in range(len(cars)):
            if len(st) == 0:
                st.append(cars[i])
            else:
                if st[-1][1] >= cars[i][1]: #check if the time at the top of the stack is greater than the current time
                    continue
                else:
                    st.append(cars[i])
        return len(st) # return the number of elements in the stack, which is the number of car fleets
