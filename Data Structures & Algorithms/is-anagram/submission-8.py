class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counter = [0] * 26
        t_counter = [0] * 26

        for i in range(len(s)):
            s_counter[ord(s[i]) - ord('a')] += 1
            t_counter[ord(t[i]) - ord('a')] += 1
        
        for i in range(len(s_counter)):
            if s_counter[i] != t_counter[i]:
                return False
        return True