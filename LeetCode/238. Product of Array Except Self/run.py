class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [1] * n
        r = [1] * n
        for i in range(1, n):
            l[i] = l[i - 1] * nums[i - 1]
            print(i, l)
        # calculate the product of elements to the right of each element
        for i in range(n - 2, -1, -1):
            r[i] = r[i + 1] * nums[i + 1]
            print(i, r)
        print(l, r)
        # calculate the product of all elements except nums[i]
        result = [l[i] * r[i] for i in range(n)]

        return result
