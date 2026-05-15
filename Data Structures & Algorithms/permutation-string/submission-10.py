class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        match_counter = [0] * 26
        L = 0
        for c in s1:
            match_counter[ord(c) - ord('a')] += 1

        def is_permutation(match_counter):
            for i in match_counter:
                if i != 0:
                    return False
            return True

        for R, c in enumerate(s2):
            match_counter[ord(c) - ord('a')] -= 1
            if R < len(s1)-1:
                continue
            if is_permutation(match_counter):
                return True
            match_counter[ord(s2[L]) - ord('a')] += 1
            L += 1
        return False
