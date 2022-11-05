class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        how_many  = []
        for i in nums:
            how_many.append(sorted_num.index(i))
        return how_many
