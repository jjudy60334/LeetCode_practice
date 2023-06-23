class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0
        while n**2 <= x:
            n += 1
        return n - 1
