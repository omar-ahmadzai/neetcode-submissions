class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        largest = 0

        for num in unique:
            if num - 1 not in unique:
                count = 1
                while num + count in unique:
                    count += 1
                if largest < count:
                    largest = count
        
        return largest