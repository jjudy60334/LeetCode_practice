class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        result = 0
        flag = 2
        while (l < r and flag == 2):
            flag = 0
            result = max(min(height[l], height[r]) * (r - l), result)
            if height[l] > height[r]:
                for i in range(r - l):
                    if height[r - i] > height[r]:
                        r = r - i
                        flag = 2
                        break
            else:
                for i in range(l + 1, r):
                    if height[i] > height[l]:
                        l = i
                        flag = 2
                        break

        return result
