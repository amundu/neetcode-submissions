class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_key(word: str) -> (str):
            chrs = [0] * 26
            for c in word:
                chrs[ord(c) - ord('a')] += 1
            return chrs

        groups = defaultdict(list)
        for word in strs:
            key = get_key(word)
            groups[tuple(key)].append(word)
        return groups.values()