class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()

        i, j = 0, len(new_str)-1
        while i<=j:
            if new_str[i] != new_str[j]:
                return False
            i+=1
            j-=1
        return True
             