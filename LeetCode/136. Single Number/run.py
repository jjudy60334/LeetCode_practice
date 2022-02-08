class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_list = []
        for i in nums:
            if i in nums_list:
                nums_list.remove(i)
            else:
                nums_list.append(i)

        return nums_list[0]
