class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0
        while n**2 <= x:
            n += 1
        return n - 1

# Use binary search


class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x + 1
        n = (l + r) // 2
        while l < r:
            n = (l + r) // 2
            if n**2 <= x and (n + 1)**2 > x:
                return n
                break
            elif n**2 > x:
                r = n
            else:
                l = n
        return n
