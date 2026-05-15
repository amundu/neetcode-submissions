class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        length = len(nums)
        l = 0

        while l + 1 < length - 1:
            if l == 0 or nums[l - 1] != nums[l]:
                m = l + 1
                r = length - 1

                while m < r:
                    if m - 1 != l and nums[m] == nums[m-1]:
                        m +=1
                        continue
                    if m - 1 != l and r != length - 1 and nums[r] == nums[r+1]:
                        r -= 1
                        continue

                    curr_sum = nums[l] + nums[m] + nums[r]
                    if curr_sum < 0:
                        m += 1
                    elif curr_sum > 0:
                        r -= 1
                    else:
                        res.append([nums[l], nums[m], nums[r]])
                        m, r = m + 1, r -1
                    
            l += 1
        return res
                        

