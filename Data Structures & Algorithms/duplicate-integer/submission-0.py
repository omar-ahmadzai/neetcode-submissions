class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length_of_nums = len(nums)

        for i in range(length_of_nums):
            for j in range(i + 1, length_of_nums):
                if nums[i] == nums[j]:
                    return True
        return False
