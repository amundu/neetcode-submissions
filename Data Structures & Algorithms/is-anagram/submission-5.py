class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars_s = Counter(s)
        chars_t = Counter(t)

        for c in chars_s.keys():
            if c not in chars_t:
                return False
            
            if chars_s[c] != chars_t[c]:
                return False
            
        return True

            


        