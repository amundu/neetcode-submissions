class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (l+1, r-1)

        output = (0, 0)
        for i in range(len(s)):
            l, r = expand(i, i)
            if output[1] - output[0] < r - l:
                output = (l, r)
            l, r = expand(i, i + 1)
            if output[1] - output[0] < r - l:
                output = (l, r)
        return s[output[0]: output[1]+1]