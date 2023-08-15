class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = []
        for i in matrix:
            m += i
        l = 0
        r = len(m) - 1
        while (l <= r and m[l] <= target and m[r] >= target):
            if m[l] < target:
                l += 1
            else:
                return True
            if m[r] > target:
                r -= 1
            else:
                return True
        return False
