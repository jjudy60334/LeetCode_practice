class Solution:
    def reverse(self, x: int) -> int:
        value = 0
        p = -1 if x < 0 else 1
        x = abs(x)
        for n, i in enumerate(str(x)):
            value += int(i) * 10**(n)
        if value <= 2**31:
            return value * p
        else:
            return 0
