class Solution:
    def isPalindrome(self, s: str) -> bool:
        process_s = [string.lower() for string in s if string.isalpha() or string.isalnum()]
        length = len(process_s)
        if length > 0:
            l = 0
            r = length - 1
            while (l < r and r > 0 and l < length - 1):
                if process_s[l] == process_s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        else:
            return True


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        process_s = [string.lower() for string in s if string.isalnum()]
        length = len(process_s)
        if length > 0:
            if process_s == process_s[-1::-1]:
                return True
            else:
                return False

        else:
            return True
