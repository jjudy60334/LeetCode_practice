class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_d = dict()
        for i in magazine:
            if i not in ran_d:
                ran_d[i] = 1
            else:
                ran_d[i] += 1
        for m in ransomNote:
            if m not in ran_d:
                return False
            elif m in ran_d and ran_d[m] == 0:
                return False
            else:
                ran_d[m] -= 1
        return True
