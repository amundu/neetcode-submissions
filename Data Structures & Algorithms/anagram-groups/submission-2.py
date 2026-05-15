class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        def get_letter_count_key(s: str) -> List[str]:
            counter = [0] * 26
            for c in s:
                counter[ord(c)-ord("a")] += 1
            return tuple(counter)

        for s in strs:
            key = get_letter_count_key(s)
            groups[key].append(s)
        
        return list(groups.values())
