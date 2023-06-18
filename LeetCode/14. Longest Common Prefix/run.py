class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_strs = len(strs)
        strs = sorted(strs)
        if len_strs == 1:
            return strs[0]
        if "" in strs:
            return ""
        else:
            r = 1
            prefix = strs[0][:r]
            ans = ""
            flag = 0
            while r <= len(strs[0]) and flag == 0:
                for st in strs[1:]:
                    if st[:r] != prefix:
                        flag = 1
                        break

                if flag == 0:
                    ans = prefix
                r += 1
                prefix = strs[0][:r]
            return ans
