class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev_chrs = set()
        res, l = 0, 0

        for r in range(len(s)):
            while s[r] in prev_chrs:
                prev_chrs.remove(s[l])
                l += 1
            prev_chrs.add(s[r])
            res = max(res, r - l + 1)
        return res
