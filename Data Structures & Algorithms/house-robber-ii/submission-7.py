class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev1, prev2 = 0, 0
        n = len(nums)
        for i in range(n-1):
            prev1, prev2 = prev2, max(prev2, nums[i] + prev1)
        max1 = prev2
        prev1, prev2 = 0, 0
        for i in range(1, n):
            prev1, prev2 = prev2, max(prev2, nums[i] + prev1)
        return max(max1, prev2)