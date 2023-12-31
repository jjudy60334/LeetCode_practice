class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        re = {'(': ')', '{': '}', '[': ']'}
        stack = []
        if len(s) < 2:
            return False
        for i in s:
            if i in re.keys():
                stack.append(i)
            else:
                k = stack.pop() if stack != [] else None
                if not k or i != re[k]:
                    return False

        return stack ==[]