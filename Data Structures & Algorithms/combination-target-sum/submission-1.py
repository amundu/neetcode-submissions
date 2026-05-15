class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(start: int, curr_combination: List[int], total: int) -> None:
            if total == target:
                res.append(curr_combination[:])
                return
            if total > target:
                return
            for i in range(start, len(nums)):
                curr_combination.append(nums[i])
                dfs(i, curr_combination, total + nums[i])
                curr_combination.pop()

        dfs(0, [], 0)
        return res
