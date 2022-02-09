class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted(nums)
        maps = {}
        for i in range(len(nums)):
            print(i)
            d = target - nums[i]
            if nums[i] not in maps:
                maps[d] = i
            else:
                return [maps[nums[i]], i]
