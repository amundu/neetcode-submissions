class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            # Get left
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Then do two pointers to find target
            L, R = i + 1, len(nums)-1
            while L < R:
                curr_sum = nums[i] + nums[L] + nums[R]
                if curr_sum < 0:
                    L += 1
                elif curr_sum > 0:
                    R -= 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
                    
        return res



