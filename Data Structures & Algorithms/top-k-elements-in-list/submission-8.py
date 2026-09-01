from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for i in nums:
            count[i] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, frequency in count.items():
            buckets[frequency].append(num)

        result = []
        for i in range(len(buckets)):
            bucket = buckets[len(buckets) - 1 - i]
            if bucket:
                result.extend(bucket)
                k -= len(bucket)

            if k == 0:
                break

        return result
