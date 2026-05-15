class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = nums[:]
        right = nums[:]

        for i in range(1, len(nums), 1):
            left[i] = left[i-1] * left[i]
        
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * right[i]

        res = nums[:]
        res[0] = right[1]
        res[-1] = left[-2]
        for i in range(1, len(nums)-1, 1):
            res[i] = left[i-1] * right[i+1]
        return res