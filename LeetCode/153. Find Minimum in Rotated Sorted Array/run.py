class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        while (l < r and mid != l and mid != r):
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
            mid = (l + r) // 2
        return min(nums[l], nums[r])
