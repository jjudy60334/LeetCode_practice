class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 1
        ans = 0
        freq = {i: 0 for i in set(s)}
        freq[s[l]] += 1
        while (l < r and r < len(s) and l >= 0):
            if r - l - max(freq.values()) <= k:
                ans = max(ans, r - l)
                freq[s[r]] += 1
                r += 1
            else:
                freq[s[l]] -= 1
                l += 1

        if r - l - max(freq.values()) <= k:
            ans = max(ans, r - l)
        return ans
