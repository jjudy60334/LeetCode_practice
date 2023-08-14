class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in sorted(nums):
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        result = sorted(count.items(), key=lambda x: -x[1])
        return [i[0] for i in result][:k]
