class Solution(object):
    def is_palindromic(self, s, h, t):
        i = 0
        while t + i <= len(s) - 1 and h - i >= 0:
            if s[h - i] != s[t + i]:
                return [h - i + 1, t + i - 1]
            i += 1
        return [h - i + 1, t + i - 1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_p = [0, 0]
        for h in range(len(s) - 1):
            palind = self.is_palindromic(s, h, h + 1)
            odd = self.is_palindromic(s, h, h)
            s_p = max([palind, odd, s_p], key=lambda x: x[1] - x[0])
        return s[s_p[0]:s_p[1] + 1]
