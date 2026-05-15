class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev_chars = set()
        longest_substring_len = 0
        L = 0
        for R, c in enumerate(s):
            while c in prev_chars:
                prev_chars.remove(s[L])
                L += 1
            prev_chars.add(c)
            longest_substring_len = max(longest_substring_len, R-L+1)

        return longest_substring_len