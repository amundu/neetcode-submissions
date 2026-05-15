class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digits_map = defaultdict(list)

        for i in range(0, ord('o') - ord('a')+1):
            digits_map[str(2+(i//3))].append(chr(ord('a')+i))
        digits_map['7'] = ['p', 'q', 'r', 's']
        digits_map['8'] = ['t', 'u', 'v']
        digits_map['9'] = ['w', 'x', 'y', 'z']
        
        def dfs(i: int, combination: List[chr]) -> None:
            if i >= len(digits):
                res.append("".join(combination))
                return
            
            for c in digits_map[digits[i]]:
                combination.append(c)
                dfs(i+1, combination)
                combination.pop()
        
        if digits != "":
            dfs(0, [])
        return res