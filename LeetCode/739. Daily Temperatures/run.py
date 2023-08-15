class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for n, i in enumerate(temperatures):
            while (stack and temperatures[stack[-1]] < i):
                result[stack[-1]] = n - stack[-1]
                stack.pop()

            stack.append(n)

        return result
