class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        set_triplets = set()
        for i, num in enumerate(nums):
            seen = {}
            for j, number in enumerate(nums):
                if j == i:
                    continue
                need = -num - number
                if need in seen and seen[need] != i and seen[need] != j:
                    triplet = tuple(sorted([need, number, num]))
                    set_triplets.add(triplet)
                else:
                    seen[number] = j
        return [list(i) for i in set_triplets]
