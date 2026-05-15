class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for s in strs:
            anagram_groups[self.get_key(s)].append(s)
        return anagram_groups.values()
        
    def get_key(self, s: str) -> tuple[int]:
        counter = [0] * 26
        for c in s:
            counter[ord(c)-ord('a')] += 1
        return tuple(counter)