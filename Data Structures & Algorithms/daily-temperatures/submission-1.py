class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                last_t, last_t_i = stack.pop()
                res[last_t_i] = i - last_t_i
            stack.append((t, i))
        return res


            
        