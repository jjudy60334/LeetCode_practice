class Solution:
    def romanToInt(self, s: str) -> int:
        symbel = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        b = 1001
        ttl = 0
        if 1 <= len(s) <= 15:
            ttl = sum(symbel[sym] for sym in s)
            for sym in s:
                if symbel[sym] > b:
                    ttl -= b * 2
                b = symbel[sym]
        return ttl
