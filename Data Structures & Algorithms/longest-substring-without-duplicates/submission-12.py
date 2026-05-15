class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev_chars = set()
        start = 0
        max_length = 0

        for c in s:
            while c in prev_chars:
                prev_chars.remove(s[start])
                start += 1
            prev_chars.add(c)
            max_length = max(max_length, len(prev_chars))
        return max_length
            