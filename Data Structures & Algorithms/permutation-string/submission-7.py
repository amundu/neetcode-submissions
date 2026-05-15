class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need_counter = Counter(s1)
        have, need = 0, len(need_counter)

        l = 0
        for r in range(len(s2)):
            if s2[r] in need_counter:
                need_counter[s2[r]] -= 1
                if need_counter[s2[r]] == 0:
                    have += 1
            if r >= len(s1):
                if s2[l] in need_counter:
                    need_counter[s2[l]] += 1
                    if need_counter[s2[l]] == 1:
                        have -= 1
                l += 1
            if have == need:
                return True
        return False

