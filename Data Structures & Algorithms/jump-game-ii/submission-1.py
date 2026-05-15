class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        jumps = 0
        while r < len(nums)-1:
            new_l = r+1
            for i in range(l, new_l):
                r = max(r, nums[i]+i)
            jumps +=1
            l = new_l
        return jumps