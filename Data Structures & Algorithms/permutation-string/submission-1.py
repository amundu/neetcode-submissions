class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        s2_counter = {}

        l = 0
        s1_len = len(s1)
        print(s1_counter)
        for r in range(len(s2)):
            s2_counter[s2[r]] = 1 + s2_counter.get(s2[r], 0)

            if r - l + 1 < s1_len:
                continue

            matches = 0
            for c, i in s1_counter.items():
                if s2_counter.get(c, 0) != i:
                    s2_counter[s2[l]] -= 1
                    l += 1
                    break
                matches+=i
            
            if matches == s1_len:
                return True
        return False 