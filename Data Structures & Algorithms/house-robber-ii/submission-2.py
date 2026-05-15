class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(loots: List[int]) -> int:
            a = b = 0
            for i in range(len(loots)):
                c = max(loots[i]+a, b)
                a, b = b, c
            return b
        return max(rob(nums[:-1]), rob(nums[1:])) if len(nums) >= 2 else nums[0]