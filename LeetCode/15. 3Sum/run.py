# O(n*n)
class Solution:
    def two_pointer(self, nums, target, n):
        nums = sorted(nums)
        l = 0
        r = len(nums) - 1
        possible = []
        while (l < r and r < len(nums) and l >= 0):
            # print (nums[l],nums[r],target)
            if l == n or r == n:
                continue
            s = target + nums[l] + nums[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                possible.append([l, r])
                l += 1

        return possible

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for n, k in enumerate(nums):
            two_point = self.two_pointer(nums, k, n)
            if len(two_point) > 0:
                for two_point_p in two_point:
                    [i, j] = two_point_p

                    if n not in two_point_p and sorted([nums[i], nums[j], k]) not in ans:
                        ans.append(sorted([nums[i], nums[j], k]))

        return sorted(ans)
