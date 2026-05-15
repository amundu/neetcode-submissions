class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_s = []
        for c in s:
            if c.isalnum():
                alpha_s.append(c.lower())
        
        l , r = 0, len(alpha_s)-1
        while l<=r:
            if alpha_s[l] != alpha_s[r]:
                return False
            l += 1
            r -= 1
        return True