class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        prev_sum = 0
        for n in nums:
            if prev_sum < 0:
                prev_sum = 0
            prev_sum += n
            max_sum = max(max_sum, prev_sum)
        return max_sum