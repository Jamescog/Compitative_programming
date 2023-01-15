"""
Question statement
==========================================================================
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
=============================================================================
Time complexity
=============================================================================
O(n)
=============================================================================
Space complexity
==============================================================================
O(n)
==============================================================================
Approach
==============================================================================
Greedy Approach
===============================================================================
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Create an array to keep track of the frequency of each task
        counter = [0]*26
        max_val = 0
        max_count = 0
        # Iterate through the input tasks
        for task in tasks:
            counter[ord(task) - ord('A')] += 1
            if max_val == counter[ord(task) - ord('A')]:
                max_count += 1
            elif max_val < counter[ord(task) - ord('A')]:
                max_val = counter[ord(task) - ord('A')]
                max_count = 1
        
        # Calculate the number of "partCount" and "partLength"
        part_count = max_val - 1
        part_length = n - (max_count - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - max_val * max_count
        idles = max(0, empty_slots - available_tasks)
        
        # Return the total time required to schedule all the tasks
        return len(tasks) + idles
