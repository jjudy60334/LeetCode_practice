class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while (len(nums1) > m):
            nums1.pop(m)
        for n in nums2:
            nums1.append(n)
        nums1.sort()
