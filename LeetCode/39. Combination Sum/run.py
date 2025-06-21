
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        count_r = []

        def count_f(l):
            return {i: l.count(i) for i in set(l)}

        def combination(root, candidates, target, comb):
            if target == 0:
                if count_f(comb) not in count_r:
                    result.append(comb)
                    count_r.append(count_f(comb))
                else:
                    return None
            else:
                for i in candidates:
                    combination(i, [k for k in candidates if k <=
                                target-i], target-i, comb+[i])

        combination(0, candidates, target, [])
        return result

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        count_r=[]
        candidates.sort()
        def combination(root, start, target, comb):
            if target==0:               
                result.append(comb)
                return 
            elif target < root:
                return 
            else:
                for n in range(start,len(candidates)):
                    combination(candidates[n],n,target-candidates[n],comb+[candidates[n]])

        combination(0,0,target,[])
        return result
    