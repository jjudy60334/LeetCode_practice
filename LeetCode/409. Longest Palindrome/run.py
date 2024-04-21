class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_s={}
        for string in s:
            if string not in count_s:
                count_s[string]=1
            else:
                count_s[string]+=1
        print (count_s)
        result=0
        odd_in_middle=0
        for k,v in count_s.items():
            if v%2==0:
                result+=v
            else:
                odd_in_middle=1
                result+=v-1
        return result+odd_in_middle