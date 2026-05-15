class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        prev_chars = defaultdict(int)
        highest_freq = 0
        L, R = 0, 0
        while R < len(s):
            prev_chars[s[R]] += 1
            while R - L + 1 - max(prev_chars.values()) > k:
                prev_chars[s[L]] -= 1
                L += 1
            highest_freq = max(highest_freq, R - L + 1)
            R += 1
        return highest_freq
