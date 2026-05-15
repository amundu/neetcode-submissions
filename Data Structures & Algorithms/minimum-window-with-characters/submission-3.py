class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        to_find = Counter(t)
        curr_chars = defaultdict(int)
        def has_all_chars():
            is_valid = True
            for c, n in to_find.items():
                if curr_chars[c] < n:
                    is_valid = False
            return is_valid     

        res = (0, float('inf'))
        start = 0
        for end, c in enumerate(s):
            if c in to_find:
                curr_chars[c] += 1
            while start <= end and has_all_chars():
                if end-start+1 < res[1]-res[0]:
                    res = (start, end+1)
                if s[start] in curr_chars:
                    curr_chars[s[start]] -= 1
                start += 1
                print(s[res[0]:res[1]], curr_chars)
            
        return "" if res[1] == float("inf") else s[res[0]:res[1]]