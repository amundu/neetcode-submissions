class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, nums[0]

        for i in range(1, len(nums)):
            prev1, prev2 = prev2, max(prev2, prev1 + nums[i])
        return prev2