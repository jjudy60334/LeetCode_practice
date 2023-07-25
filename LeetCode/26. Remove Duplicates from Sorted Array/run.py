class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = []
        i = 0
        while i < len(nums):
            if nums[i] == '_':
                break
            elif nums[i] in a:
                nums.pop(i)
                nums.append('_')
            else:
                a.append(nums[i])
                i += 1

        return len(a)
