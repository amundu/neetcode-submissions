class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_length = 1
        dp = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            local_max = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    local_max = max(local_max, dp[j] + 1)
            dp[i] = local_max
            max_length = max(max_length, dp[i])
        return max_length
            
                