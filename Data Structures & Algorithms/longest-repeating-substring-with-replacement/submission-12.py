class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        prev_chars = defaultdict(int)
        max_length = 0
        max_freq = 0

        for r, c in enumerate(s):
            prev_chars[c] += 1
            max_freq = max(max_freq, prev_chars[c])

            if (r-l+1) - max_freq > k:
                prev_chars[s[l]] -= 1
                l += 1
            max_length = max(max_length, r-l+1)
        return max_length