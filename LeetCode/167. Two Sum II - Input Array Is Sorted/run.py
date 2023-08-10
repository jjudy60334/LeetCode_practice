class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while (l < r and l < len(numbers) and r > 0):
            sum_n = numbers[l] + numbers[r]
            if sum_n < target:
                l += 1
            elif sum_n > target:
                r -= 1
            else:
                return [l + 1, r + 1]
