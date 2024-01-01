class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted([string for string in s]) == sorted([string for string in t])