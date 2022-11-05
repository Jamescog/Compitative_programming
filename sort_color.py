class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            while nums[i - 1] > nums[i]  and i > 0:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                i -= 1
        return nums
