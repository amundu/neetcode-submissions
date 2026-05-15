class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        prev1, prev2 = 0, 0
        for n in nums:
            prev1, prev2 = prev2, max(prev2, n + prev1)
        return prev2