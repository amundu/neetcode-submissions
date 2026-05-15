class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for n in nums:
            c = max(n + a, b)
            a, b = b, c
        return b