class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_str_key(s: str) -> (int):
            key = [0] * 26
            for c in s:
                key[ord(c)-ord('a')] += 1
            return tuple(key)


        anagrams = defaultdict(list)
        # for every str get str key
        for s in strs:
            # may keys to str to group them
            anagrams[get_str_key(s)].append(s)
        # return map values
        return anagrams.values()