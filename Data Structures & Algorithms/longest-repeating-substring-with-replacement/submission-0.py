class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 1
        char_freqs = [0] * 26
        
        l, r = 0, 0
        while r < len(s):
            char_freqs[ord(s[r]) - ord('A')] += 1
            max_freq = max(char_freqs)
            curr_len = r - l + 1

            while curr_len - max_freq > k:
                char_freqs[ord(s[l]) - ord('A')] -= 1
                max_freq = max(char_freqs)
                l += 1
                curr_len = r - l + 1
            
            r+=1
            max_len = max(max_len, curr_len)
        return max_len
                
