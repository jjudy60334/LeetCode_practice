
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums3 = nums2 + nums1
        nums3 = sorted(nums3)
        if len(nums3) % 2 == 0:
            f = int(floor((len(nums3) + 1) / 2.0))
            c = f - 1
            return (nums3[f] + nums3[c]) / 2.0
        else:
            p = (len(nums3) + 1) / 2 - 1
            return nums3[p]
