"""
Date: Jan 10 2023
File: leetcode_P1561.py
Author: Yaekob Demisse


Question Statement
There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have.

Time Complexity
=====================================
O(n log n)
=====================================
Space Complexity
=====================================
O(1)
======================================
Approach
======================================
Greedy Algorithm

"""
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # Sort the piles
        piles.sort()
        # If the length of the piles is 3, return the 2nd element
        if len(piles) == 3:
            return piles[1]

        # Initialize necessary variables
        max_coins = 0
        count = 0
        last_pile_index = len(piles) - 2

        # Loop through the coins 
        while last_pile_index >= 0 and count < len(piles) // 3:
            max_coins += piles[last_pile_index]
            last_pile_index -= 2
            count += 1
        
        # Return the max_coins
        return max_coins

        
