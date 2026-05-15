class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict(list)

        def get_key(s: str) -> List[int]:
            key = [0]*26
            for c in s:
                key[ord(c) - ord('a')] += 1
            return key
        
        for s in strs:
            grouped_anagrams[tuple(get_key(s))].append(s)
        return list(grouped_anagrams.values())
