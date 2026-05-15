class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        chars_freqs = defaultdict(int)
        max_freq = 0

        l = 0
        for r in range(len(s)):
            chars_freqs[s[r]] += 1
            max_freq = max(max_freq, chars_freqs[s[r]])
            if (r-l+1) - max_freq > k:
                chars_freqs[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
        