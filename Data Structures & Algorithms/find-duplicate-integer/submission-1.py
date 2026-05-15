class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i, n in enumerate(nums):
            if i ==0:
                continue
            if nums[i] == nums[i-1]:
                return n