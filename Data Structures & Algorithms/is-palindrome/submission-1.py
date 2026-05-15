class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = {}
        for i in range(26):
            valid_chars[chr(ord('a') + i)] = chr(ord('a') + i)
            valid_chars[chr(ord('A') + i)] = chr(ord('a') + i)
        for i in range(10):
            valid_chars[str(i)] = str(i)
        i, j = 0, len(s) - 1
        while i <= j:
            is_i_valid = s[i] in valid_chars
            is_j_valid = s[j] in valid_chars
            if not is_i_valid:
                i += 1
            if not is_j_valid:
                j -= 1
            if is_i_valid and is_j_valid:
                if valid_chars[s[i]] != valid_chars[s[j]]:
                    return False
                else:
                    i += 1
                    j -= 1

        return True
             