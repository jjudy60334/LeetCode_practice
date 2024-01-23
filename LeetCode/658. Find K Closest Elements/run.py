
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0  # the index of left element in the arr  of the answer
        r = len(arr)-1  # the index of right element in the arr of the answer
        # l=0 r=4
        # left elment=1 right element=5
        while (r+1-l > k):
            # left difference:2 right diff:2
            # 2 iter: index l=0 r=3 element: l=1 r=4
            if abs(x-arr[l]) > abs(x-arr[r]):
                l += 1
            else:
                r -= 1
        return arr[l:r+1]
