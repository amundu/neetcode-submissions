class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        s2_counter = {}

        l = 0
        s1_len = len(s1)
        matches = 0
        for r in range(len(s2)):
            s2_counter[s2[r]] = 1 + s2_counter.get(s2[r], 0)

            if s2_counter[s2[r]] == s1_counter.get(s2[r], 0):
                matches += 1

            if r - l + 1 < s1_len:
                continue

            if matches == len(s1_counter):
                return True
            
            if s2_counter[s2[l]] == s1_counter.get(s2[l], 0):
                matches -= 1
            s2_counter[s2[l]] -= 1
            l += 1
        return False 