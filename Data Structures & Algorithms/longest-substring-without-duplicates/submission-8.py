class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev_chars = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in prev_chars:
                prev_chars.remove(s[l])
                l += 1
            prev_chars.add(s[r])
            res = max(res, len(prev_chars))
        return res
            

