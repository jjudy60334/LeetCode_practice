class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alpha = sorted([s for s in s1])
        l = 0
        r = l
        while r < len(s2) and l + len(s1) <= len(s2):
            if s2[r] in alpha:
                r += 1
                l = r - len(s1)
            else:
                l = r + 1
                r = l + len(s1)
            if sorted(s2[l:r]) == alpha:
                return True

        return False
