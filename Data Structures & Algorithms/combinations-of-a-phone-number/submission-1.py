class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digits_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        output = []
        path = []
        def dfs(idx):
            if idx == len(digits):
                output.append("".join(path))
                return
            for c in digits_to_letters[digits[idx]]:
                path.append(c)
                dfs(idx+1)
                path.pop()
        dfs(0)
        return output