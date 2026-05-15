class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.longest_palindrome = ""

        for i in range(len(s)):
            # Odd
            self.expand(i, i, s)
            
            # Even
            self.expand(i, i+1, s)
        return self.longest_palindrome
    
    def expand(self, left: int, right: int, s: str) -> None:
        while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
            if len(self.longest_palindrome) < right - left + 1:
                self.longest_palindrome = s[left: right + 1] 
            left -= 1
            right += 1
            
            
    