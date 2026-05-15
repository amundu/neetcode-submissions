class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        prev_chars = set()
        max_len = 0
        for c in s:
            while c in prev_chars:
                prev_chars.remove(s[start])
                start += 1
            prev_chars.add(c)
            max_len = max(max_len, len(prev_chars))
        return max_len