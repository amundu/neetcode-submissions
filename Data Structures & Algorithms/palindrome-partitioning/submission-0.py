class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []
        
        def backtrack(i: int) -> None:
            if i >= len(s):
                res.append(partition.copy())
                return
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    partition.append(s[i:j+1])
                    backtrack(j+1)
                    partition.pop()
        backtrack(0)
        return res
    
    def is_palindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True
