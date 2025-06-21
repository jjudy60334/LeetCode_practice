class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        l = len(candidates)
        result = []

        def backtrack(start, target, comb):
            if target == 0:
                last_suc = comb[0]
                result.append(comb)
                return None
            elif target < 0:
                return None
            else:
                for i in range(start, l):
                    if target < candidates[i]:
                        continue
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    backtrack(i+1, target-candidates[i], comb+[candidates[i]])
        backtrack(0, target, [])
        return result
