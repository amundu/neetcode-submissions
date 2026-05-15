class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        [(40,5),(38, 1)]
        '''
        stack = []

        output = []
        for i in range(len(temperatures)-1, -1, -1):
            temp = temperatures[i]
            while stack and stack[-1][0] <= temp:
                stack.pop()
            
            output.append(stack[-1][1] - i if stack else 0)
            stack.append((temp, i))
        return output[::-1]
            