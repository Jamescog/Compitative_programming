"""
# Question
You are given a 0-indexed array nums of distinct integers. You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.

More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

Return any rearrangement of nums that meets the requirements.
# Approach
- Sort the input array in ascending order.
- Initialize two variables i and j to 0 and len(nums) - 1, respectively.
- Loop until i is greater than j.
- Append the element at index i in the input array to the rearranged array.
- Increment i by 1.
- If i is still less than or equal to j, append the element at index j in the input array to the rearranged array.
- Decrement j by 1.
- Return the rearranged array.

# Complexity
- Time complexity:
```
O(n * log(n))
```

- Space complexity:
```
 O(n)
```

# Code
"""
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # sort the array in ascending order
        nums.sort()
        # create a new array to store the rearranged elements
        rearranged = []
        # start with the smallest element
        i = 0
        # start with the largest element
        j = len(nums) - 1
        # loop until there are no more elements to add
        while i <= j:
            # add the smallest element to the rearranged array
            rearranged.append(nums[i])
            i += 1
            # if there are still elements left, add the largest element to the rearranged array
            if i <= j:
                rearranged.append(nums[j])
                j -= 1
        return rearranged
