class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        left_total = nums[0]
        right_total = nums[-1]
        for i in range(1, len(nums)):
            left[i] = left_total
            left_total *= nums[i]
            right[-1-i] = right_total
            right_total *= nums[-1-i]
        return [left[i] * right[i] for i in range(len(nums))]