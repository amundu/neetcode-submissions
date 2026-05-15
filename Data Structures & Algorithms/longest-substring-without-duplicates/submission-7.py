class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev_chars = set()
        l, r = 0, 0
        max_len = 0
        while r < len(s):
            while s[r] in prev_chars:
                    prev_chars.remove(s[l])
                    l += 1

            prev_chars.add(s[r])
            max_len = max(max_len,len(prev_chars))
            r += 1
        return max_len

