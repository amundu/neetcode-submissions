class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        res = [0] * (len(num1)+ len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num2)):
            for j in range(len(num1)):
                res[i+j] += (int(num2[i]) * int(num1[j])) 
                res[i+j+1] += res[i+j] // 10
                res[i+j] = res[i+j] % 10
        beg_zeros = 0
        res = res[::-1]
        while beg_zeros < len(res) and res[beg_zeros] == 0:
            beg_zeros += 1
        res = map(str, res[beg_zeros:])
        return "".join(res)