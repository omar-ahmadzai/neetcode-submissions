class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for ind, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                stack_ind = stack.pop()
                result[stack_ind] = ind - stack_ind

            stack.append(ind)

        return result
