class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(curr, idx):
            if idx == len(nums):
                res.append(curr[:])
                return
            
            curr.append(nums[idx])
            backtrack(curr, idx + 1)
            curr.pop()
            idx += 1
            while idx < len(nums) and nums[idx-1] == nums[idx]:
                idx += 1
            backtrack(curr, idx)
                
        backtrack([], 0)
        return res