class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) > 1:
            return self.subsets(nums[:-1]) + [n + [nums[-1]] for n in self.subsets(nums[:-1])]
        else:
            return [nums, []]
