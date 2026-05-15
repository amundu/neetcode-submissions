class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev_chrs = set()
        longest_len, start_idx = 0, 0

        for i, c in enumerate(s):
            if c in prev_chrs:
                longest_len = max(longest_len, i - start_idx)
                for j in range(start_idx, i):
                    if s[j] != c:
                        prev_chrs.remove(s[j])
                    else:
                        start_idx = j + 1
                        break
            else:
                prev_chrs.add(c)
        
        longest_len = max(longest_len, len(s) - start_idx)
        return longest_len
