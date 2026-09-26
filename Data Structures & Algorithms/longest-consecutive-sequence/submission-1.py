class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        not_checked = set(nums)

        max = 0
        for num in nums:
            if num not in not_checked:
                continue

            # 1 is set because a number alone has one length
            sequence_length = 1

            bigger = num+1
            # Checking for the numbers bigger
            while bigger in not_checked:
                not_checked.remove(bigger)
                sequence_length += 1
                bigger += 1

            smaller = num-1
            while smaller in not_checked:
                not_checked.remove(smaller)
                sequence_length += 1
                smaller -= 1

            if max < sequence_length:
                max = sequence_length

        return max

