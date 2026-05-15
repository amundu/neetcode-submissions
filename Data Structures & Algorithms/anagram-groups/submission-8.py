class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_key(s: str) -> tuple[int]:
            key = [0] * 26
            for c in s:
                key[ord(c)-ord('a')] += 1
            return tuple(key)

        res = defaultdict(list)
        for s in strs:
            s_key = get_key(s)
            res[s_key].append(s)
        return res.values()