class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        curr_prefix = nums[0]

        for i in range(1, n):
            res[i] = curr_prefix
            curr_prefix *= nums[i]

        curr_suffix = nums[-1]
        for i in range(n-2, -1, -1):
            res[i] *= curr_suffix
            curr_suffix *= nums[i]
        return res