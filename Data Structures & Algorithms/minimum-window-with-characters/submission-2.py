class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need_counter = Counter(t)
        have, need = 0, len(need_counter)
        res_l, res_r = 0, float('inf')

        l = 0
        for r in range(len(s)):
            if s[r] in need_counter:
                need_counter[s[r]] -= 1
                if need_counter[s[r]] == 0:
                    have += 1
            while have == need:
                if res_r - res_l > r - l:
                    res_l = l
                    res_r = r
                if s[l] in need_counter:
                    need_counter[s[l]] += 1
                    if need_counter[s[l]] == 1:
                        have -= 1
                l += 1
        
        return s[res_l: res_r+1] if res_r != float('inf') else ""

