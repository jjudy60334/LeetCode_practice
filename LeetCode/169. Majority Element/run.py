class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        j = dict()
        max_n = 0
        for i in nums:
            if i not in j:
                j[i] = 0
            if j[i] > length / 2:
                return i
            else:
                j[i] += 1
                max_n = max(max_n, j[i])

        return [key for key in j if j[key] == max_n][0]
