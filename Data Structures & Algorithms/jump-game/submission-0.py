class Solution:
    def canJump(self, nums: List[int]) -> bool:
        required_jumps = 1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] >= required_jumps:
                required_jumps = 0
            required_jumps += 1
        return required_jumps == 1
