class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_count = Counter(t)
        l = r = 0
        matches = len(t_count)
        curr_matches = 0
        res = [-1, len(s)]
        s_count = defaultdict(int)

        for r in range(len(s)):
            c = s[r]
            s_count[c] += 1
            if c in t_count and s_count[c] == t_count[c]:
                curr_matches += 1

            while curr_matches == matches:
                res = res if res[1]-res[0] < r-l+1 else (l,r+1)
                c = s[l]
                s_count[c] -= 1
                if c in t_count and s_count[c] < t_count[c]:
                    curr_matches -= 1
                l += 1

        return s[res[0]: res[1]] if res[0] != -1 else ""

