"""
# Question
You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.

Return the string that represents the kth largest integer in nums.

Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.
# Approach
- The first line uses a list comprehension to convert all elements in the list nums to integers. The resulting list is stored in nums.
- The second line sorts the list in descending order. The reverse parameter is set to True, which sorts the list in descending order.
- The third line returns the k-th largest element as a string. The k-1 index is used because list indices start at 0.

---


# Complexity
- Time complexity:
```
O(nlog(n))
```

- Space complexity:
```
O(n)
```

# Code
"""
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
       # Convert all elements in the list to integers
        nums = [int(x) for x in nums]
        # Sort the list in descending order
        nums.sort(reverse=True)
        # Return the k-th largest element
        return str(nums[k-1])
