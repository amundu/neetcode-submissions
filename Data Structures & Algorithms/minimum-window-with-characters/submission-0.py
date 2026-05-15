class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""

        window, t_map = {}, Counter(t)
        have, need = 0, len(t_map)
        res, res_len = [-1,-1], float('inf')
        l= 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in t_map and window[c] == t_map[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                window[s[l]] -= 1
                if s[l] in t_map and window[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if res_len != float('inf') else ""