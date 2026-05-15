class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        prev_chars = defaultdict(int)
        L = 0
        res = 0
        max_f = 0
        for R, c in enumerate(s):
            prev_chars[c] += 1
            max_f = max(max_f, prev_chars[c])
            while (R - L + 1) - max_f > k:
                prev_chars[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)
        return res
                