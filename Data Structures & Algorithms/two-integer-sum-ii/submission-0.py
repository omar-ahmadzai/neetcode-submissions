class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first_ind = 0
        last_ind = len(numbers) - 1

        while first_ind < last_ind:
            result = numbers[first_ind] + numbers[last_ind]

            if result == target:
                return [first_ind + 1, last_ind + 1]
            elif result < target:
                first_ind += 1
            else:
                last_ind -= 1
        