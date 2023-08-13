class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        # print (nums,target)
        while (nums[l] <= target and nums[r] >= target):

            if nums[l] < target:
                l += 1
            elif nums[l] == target:
                return l
            if nums[r] > target:
                r -= 1
            elif nums[r] == target:
                return r
        return -1
