class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_msg = [f"{len(s)}#{s}" for s in strs]
        return "".join(encoded_msg)

    def decode(self, s: str) -> List[str]:
        
        n = 0
        decoded_list = []
        start = i = 0
        while i < len(s):
            while s[i] != "#":
                i += 1
                continue
            n = int(s[start:i])
            i += 1
            decoded_list.append(s[i:i+n])
            start = i = i + n
        return decoded_list