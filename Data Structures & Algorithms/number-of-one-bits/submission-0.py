class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = 1 << i
            res += int((bit & n) > 0)
        return res