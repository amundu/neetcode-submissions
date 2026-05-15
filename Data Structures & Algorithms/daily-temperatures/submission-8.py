class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (i, t)
        results = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop()
            
            if stack:
                results[i] = stack[-1][0] - i
            stack.append((i, temperatures[i]))
        return results

