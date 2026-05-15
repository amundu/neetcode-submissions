class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        prev_chars = defaultdict(int)
        highest_freq = 0
        max_f = 0
        L = 0
        for R in range(len(s)):
            prev_chars[s[R]] += 1
            max_f = max(max_f, prev_chars[s[R]])
            while R - L + 1 - max_f > k:
                prev_chars[s[L]] -= 1
                L += 1
            highest_freq = max(highest_freq, R - L + 1)
        return highest_freq
