class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        if target not in nums:
            return []
        idx  = sorted_nums.index(target)
        result = []
        count = sorted_nums.count(target)
        if count == 1:
            result.append(idx)
        else:
            for i in range(idx, idx + count):
                result.append(i)
        return result
