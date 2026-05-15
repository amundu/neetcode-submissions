class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_count = Counter(t)
        l = 0
        matches = len(t_count)
        curr_matches = 0
        res = None
        s_count = defaultdict(int)
        for r in range(len(s)):
            while curr_matches == matches:
                res = res if res and res[1]-res[0] < r-l else (l,r)
                c = s[l]
                if c in t_count:
                    s_count[c] -= 1
                    if s_count[c] < t_count[c]:
                        curr_matches -= 1
                l += 1
            c = s[r]
            if c not in t_count:
                continue
            s_count[c] += 1
            if s_count[c] == t_count[c]:
                curr_matches += 1
        
        r = len(s)
        while l < r and curr_matches == matches:
            res = res if res and res[1]-res[0] < r-l else (l,r)
            c = s[l]
            if c in t_count:
                s_count[c] -= 1
                if s_count[c] < t_count[c]:
                    curr_matches -= 1
            l += 1
        return s[res[0]: res[1]] if res else ""

