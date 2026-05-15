class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 1
        char_freqs = [0] * 26
        
        l, r = 0, 0
        for r in range(len(s)):
            char_freqs[ord(s[r]) - ord('A')] += 1

            while r - l + 1 - max(char_freqs) > k:
                char_freqs[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        return max_len
                
