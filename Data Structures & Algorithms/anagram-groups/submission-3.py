class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        def sort_string(s: str) -> str:
            chars = [0] * 26
            key = ""
            for c in s:
                chars[ord(c) - ord('a')] += 1
            
            for i in range(len(chars)):
                key += chr(ord('a') + i) * chars[i]
            return key

        for s in strs:
            key = sort_string(s)
            groups[key].append(s)
        
        return list(groups.values())