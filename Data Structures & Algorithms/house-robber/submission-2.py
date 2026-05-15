class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.insert(0,0)
        for i in range(3, len(nums)):
            nums[i] += max(nums[i-2], nums[i-3]) 
        print(nums)
        return max(nums[-1], nums[-2])