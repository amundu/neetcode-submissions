class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        freqs_map = defaultdict(int)
        def get_most_frequent_element():
            most_freq_element = None
            for e, freq in freqs_map.items():
                if most_freq_element == None or freqs_map[most_freq_element] < freq:
                    most_freq_element = e
            return most_freq_element

        for r in range(len(s)):
            freqs_map[s[r]] += 1
            most_freq_element = get_most_frequent_element()
            while (r-l+1) - freqs_map[most_freq_element] > k:
                freqs_map[s[l]] -= 1
                l += 1
                most_freq_element = get_most_frequent_element()
            res = max(res, r - l + 1)
        return res
        