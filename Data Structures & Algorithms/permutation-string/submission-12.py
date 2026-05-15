class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        chars_to_find = [0] * 26
        prev_chars = [0] * 26
        for i in range(len(s1)):
            chars_to_find[ord(s1[i]) - ord('a')] += 1
            prev_chars[ord(s2[i]) - ord('a')] += 1

        matches = len(chars_to_find)
        for i in range(len(chars_to_find)):
            if chars_to_find[i] - prev_chars[i] == 0:
                matches -= 1
        for i in range(len(s1), len(s2)):
            if matches == 0:
                return True
            remove_i = ord(s2[i-len(s1)]) - ord('a')
            if prev_chars[remove_i] == chars_to_find[remove_i]:
                matches += 1
            prev_chars[remove_i] -= 1
            if prev_chars[remove_i] == chars_to_find[remove_i]:
                matches -= 1
            add_i = ord(s2[i]) - ord('a')

            if prev_chars[add_i] == chars_to_find[add_i]:
                matches += 1
            prev_chars[add_i] += 1
            if prev_chars[add_i] == chars_to_find[add_i]:
                matches -= 1
        return matches == 0
