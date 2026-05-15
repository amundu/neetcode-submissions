class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        prev_chars = defaultdict(int)
        longest_substring_len = 0

        def get_most_freq_element() -> str:
            most_freq_element = None
            for c, freq in prev_chars.items():
                if most_freq_element is None or prev_chars[most_freq_element] < freq:
                    most_freq_element = c
            return most_freq_element


        highest_freq = 0
        L, R = 0, 0
        while R < len(s):
            prev_chars[s[R]] += 1
            most_freq_element = get_most_freq_element()
            while R - L + 1 - prev_chars[most_freq_element] > k:
                prev_chars[s[L]] -= 1
                L += 1
                most_freq_element = get_most_freq_element()
            highest_freq = max(highest_freq, R-L+1)
            R += 1
        return highest_freq
