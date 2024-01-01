class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while (l <= r):
            m = (l+r)//2
            n_m = nums[m]
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if l == r-1:
                return -1
            if target > n_m:
                l = m
                r -= 1
            elif target < n_m:
                r = m
                l += 1
            else:
                return m

        return -1


# recursive
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        def binary_search(l, r):
            if l > r:
                return -1
            m = (l+r)//2
            n_m = nums[m]
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if target == n_m:
                return m
            elif target < n_m:
                return binary_search(l+1, m)
            else:
                return binary_search(m, r-1)
        return binary_search(l, r)
