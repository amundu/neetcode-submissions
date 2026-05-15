class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        def reduce_window():
            nonlocal l, r, curr_matches, res
            while curr_matches == matches:
                res = res if res and res[1]-res[0] < r-l else (l,r)
                c = s[l]
                if c in t_count:
                    s_count[c] -= 1
                    if s_count[c] < t_count[c]:
                        curr_matches -= 1
                l += 1

        t_count = Counter(t)
        l = r = 0
        matches = len(t_count)
        curr_matches = 0
        res = None
        s_count = defaultdict(int)

        for r in range(len(s)):
            reduce_window()
            c = s[r]
            r += 1
            if c not in t_count:
                continue
            s_count[c] += 1
            if s_count[c] == t_count[c]:
                curr_matches += 1

        reduce_window()
        return s[res[0]: res[1]] if res else ""

