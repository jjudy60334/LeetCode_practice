class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        else:
            left = 0
            right = len(nums) - 1
            l1 = 0
            r1 = 0
            while(left >= 0 and right <= len(nums) - 1 and (l1 == 0 or r1 == 0)):
                if nums[left] < target:
                    left += 1
                else:
                    l1 = 1
                if nums[right] > target:
                    right -= 1
                else:
                    r1 = 1
        return [left, right]
