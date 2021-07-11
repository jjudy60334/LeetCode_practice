class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        group = numRows + numRows - 2
        if group <= 0:
            return s
        show = {k: [] for k in range(group)}
        return_string = ""
        pos = {i: numRows + (numRows - (i + 1)) - 1 if i > numRows - 1 else i for i in range(group)}
        for i in range(len(s)):
            show[pos[(i) % group]].append(s[i])
        for j in range(group):

            return_string += "".join(show[j])
        return return_string
