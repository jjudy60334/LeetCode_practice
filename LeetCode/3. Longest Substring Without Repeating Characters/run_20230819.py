class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        if len(s) <= 1:
            return len(s)
        ans = 0
        for n, string in enumerate(s[1:]):
            if string in s[l:r]:
                ans = max(ans, r - l)
                l = s[l:r].index(string) + l + 1
            r += 1
        ans = max(ans, r - l)
        return ans
