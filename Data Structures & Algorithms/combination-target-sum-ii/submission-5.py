class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        num_counter = Counter(candidates)
        candidates = list(num_counter.keys())
        res = []
        def dfs(i, curr, total):
            if total == target:
                res.append(curr[::])
                return
            if total > target or i == len(candidates):
                return

            if num_counter[candidates[i]] > 0:
                num_counter[candidates[i]] -= 1
                curr.append(candidates[i])
                dfs(i, curr, total + candidates[i])
                num_counter[candidates[i]] += 1
                curr.pop()
            dfs(i + 1, curr, total)
        dfs(0, [], 0)
        return res