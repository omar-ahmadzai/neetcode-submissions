class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = defaultdict(list)
        for i in set(nums):
            dct[nums.count(i)].append(i)
        keys = sorted(dct.keys(), reverse=True)
        k_frequent = []
        for key in keys:
            k_frequent.extend(dct[key])
            if len(k_frequent) >= k:
                break
        return k_frequent[:k]
