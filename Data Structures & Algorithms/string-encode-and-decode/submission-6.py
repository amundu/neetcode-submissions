class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs:
            output.append(f"{len(word)}#{word}")
        return ''.join(output)


    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            n = int(s[i:j])
            j += 1
            output.append(s[j: j+n])
            i = j + n
        return output