class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        start = 0
        while start < len(nums):
            if start != 0 and nums[start] == nums[start-1]:
                start += 1
                continue
            L = start + 1
            R = len(nums)-1
            while L < R:
                curr = nums[start] + nums[L] + nums[R]
                if curr < 0:
                    L += 1
                elif curr > 0:
                    R -= 1
                else:
                    res.append([nums[start], nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
            start += 1
            
        return res