class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def dfs(idx):
            if idx == len(nums):
                res.append(nums[:])
                return
            for i in range(idx, len(nums)):
                swap(idx, i)
                dfs(idx+1)
                swap(idx, i)

        dfs(0)
        return res