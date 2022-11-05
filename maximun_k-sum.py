class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        low = 0
        high = len(nums) - 1
        operations = 0
        nums.sort()
        while (low < high):
            sum = nums[low]  + nums[high]
            if sum == k:
                operations += 1
                low += 1
                high -= 1
            elif(sum > k):
                high -= 1
            else:
                low += 1
        return operations
