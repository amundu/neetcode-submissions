class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def decision(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(decision(i+2) + nums[i], decision(i+1))
            return cache[i]
        return decision(0)