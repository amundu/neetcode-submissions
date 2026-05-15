class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        prev_chars = defaultdict(int)
        start = 0
        res = 0
        for i, c in enumerate(s):
            prev_chars[c] += 1
            curr_max = max(prev_chars.values())
            while i - start - curr_max + 1 > k:
                prev_chars[s[start]] -= 1
                start += 1
                curr_max = max(prev_chars.values())
            res = max(res, i - start + 1)
        return res
                