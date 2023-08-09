class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        for string in strs:
            str_ = "".join(sorted([it for it in string]))
            if str_ not in result.keys():
                result[str_] = [string]
            else:
                result[str_].append(string)
        return result.values()
