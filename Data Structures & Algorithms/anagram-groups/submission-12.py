class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        def get_key(word):
            key = [0] * 26
            for c in word:
                key[ord(c) - ord('a')] += 1
            return tuple(key)

        for word in strs:
            groups[get_key(word)].append(word)
        
        return [group for group in groups.values()]