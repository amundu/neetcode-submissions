class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            if not stack:
                stack.append((t, i))
                continue
            
            while stack and stack[-1][0] < t:
                last_t, last_t_i = stack.pop()
                res[last_t_i] = i - last_t_i
            stack.append((t, i))
        
        while stack:
            last_t, last_t_i = stack.pop()
            res[last_t_i] = 0
        return res


            
        