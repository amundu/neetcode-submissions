class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            curr = nums[i-2] + nums[i] if i >= 2 else nums[i]
            nums[i] = max(nums[i-1], curr)
        return nums[-1]