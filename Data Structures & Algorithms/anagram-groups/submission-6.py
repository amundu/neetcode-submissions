class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_key(word: str) -> (int):
            bucket = [0] * 26
            for c in word:
                bucket[ord(c)-ord('a')] += 1
            return tuple(bucket)
        
        groups = defaultdict(list)
        for word in strs:
            groups[get_key(word)].append(word)
        return groups.values()