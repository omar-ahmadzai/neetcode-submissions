class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_counter = 0

        for i, num in enumerate(nums):

            if num == 0:
                if zero_counter == 1:
                    return [0] * len(nums)
                zero_counter += 1
                zero_index = i
                continue

            product *= num

        if zero_counter == 1:
            result = [0] * len(nums)
            result[zero_index] = product
            return result

        result = []
        for i in nums:
            result.append(int(product/i))
        return result
