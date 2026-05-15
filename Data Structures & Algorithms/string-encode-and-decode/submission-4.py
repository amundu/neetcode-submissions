class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            if s == "":
                res += "0#"
            else:
                res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            n_str = ""
            while s[i] != '#':
                n_str += s[i]
                i+=1
            i+=1
            n = int(n_str)
            if n == 0:
                res.append("")
            else: 
                res.append(s[i:i + n])
            i = i + n
        
        return res