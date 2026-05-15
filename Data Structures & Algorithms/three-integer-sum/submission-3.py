class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        # -4, -1, -1, 0, 1 , 2
        #      i      l      r
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            l, r = i + 1, len(nums)-1
            while l < r:
                a, b = nums[l], nums[r]
                curr_sum = n + a + b
                if curr_sum == 0:
                    res.append([n, a, b])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1
        return res

