class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def get_key(s):
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            return tuple(key)

        res = defaultdict(list)
        for s in strs:
            res[get_key(s)].append(s)
        return [v for v in res.values()]