class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = nums.count(0)
        
        for num in nums:
            if num != 0:
                product *= num
        
        if zero_count == 1:
            return [product if num == 0 else 0 for num in nums]
        elif zero_count > 1:
            return [0 for _ in nums]
        else:
            return [int(product/num) for num in nums]

        