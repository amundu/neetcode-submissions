class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        def get_letter_count_key(s: str) -> List[str]:
            counter = [0] * 26
            for c in s:
                counter[ord(c)-97] += 1
            return tuple(counter)

        for s in strs:
            key = get_letter_count_key(s)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        
        return list(groups.values())
