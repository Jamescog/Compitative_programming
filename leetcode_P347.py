"""
Question statement
===============================
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
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
Brute force
===============================
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create the counter

        count = {}

        for i in nums:
            if i in count:
                count[i]  += 1
            else:
                count[i] = 1
        # Sort the count
        sorted_count = sorted(count.items(), key=lambda x:x[1],reverse=True)
        
        # return the first K elements from the tuple
        return [i[0] for i in sorted_count[:k]]
