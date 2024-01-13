# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=0
        r=n
        m=(l+r)//2
        while (l<r and l!=m and r!=m):
            if isBadVersion(m):
                r=m
            else:
                l=m
            m=(l+r)//2
        return m if isBadVersion(m) and not isBadVersion(r) else r