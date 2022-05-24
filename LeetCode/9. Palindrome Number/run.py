class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        l = [i for i in str(x)]
        r_l = list(reversed(l))

        return l == r_l and '-' not in l
