class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        chars_to_find = [0] * 26
        prev_chars = [0] * 26
        for i in range(len(s1)):
            chars_to_find[ord(s1[i]) - ord('a')] += 1
            prev_chars[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s1), len(s2)):
            if chars_to_find == prev_chars:
                return True
            prev_chars[ord(s2[i-len(s1)]) - ord('a')] -= 1
            prev_chars[ord(s2[i]) - ord('a')] += 1
        return chars_to_find == prev_chars
