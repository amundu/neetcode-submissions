class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr_combination = []
        def dfs(i: int, prev_sum: int) -> None:
            if i == len(nums) or prev_sum > target:
                return
            if prev_sum == target:
                res.append(curr_combination[:])
                return
            curr_combination.append(nums[i])
            dfs(i, prev_sum + nums[i])
            curr_combination.pop()
            dfs(i+1, prev_sum)

        dfs(0, 0)
        return res
