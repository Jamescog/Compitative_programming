"""
# Question
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.
# Approach
- Extract the subarray from the given array nums using the indices l[i] and r[i] as the start and end indices.
- Sort the subarray in ascending order.
- Calculate the difference between the first and last element in the sorted subarray. If the difference is zero, then the subarray has only one element and it can be considered as an arithmetic sequence.
- If the difference is non-zero, then calculate the common difference by dividing the difference by the number of elements in the subarray minus one.
- Check if all the elements in the sorted subarray can be obtained by adding the common difference to the first element. If this is the case, then the subarray can be rearranged to form an arithmetic sequence. If not, then it cannot be rearranged to form an arithmetic sequence.
# Complexity
- Time complexity:
    O(nm)

- Space complexity:
    O(1)

"""
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArithmetic(arr):
            if len(arr) == 1:
                return True
            diff = arr[-1] - arr[0]
            common_diff = diff / (len(arr) - 1)
            for i in range(1, len(arr)):
                if arr[i] - arr[i-1] != common_diff:
                    return False
            return True

        answer = []
        for i in range(len(l)):
            subarray = nums[l[i]:r[i]+1]
            subarray.sort()
            answer.append(isArithmetic(subarray))
        return answer
