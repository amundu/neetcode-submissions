class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        prev = set()
        def dfs(i, curr, total):
            if total == target:
                if tuple(curr) not in prev:
                    prev.add(tuple(curr))
                    res.append(curr[::])
                return
            if total > target or i == len(candidates):
                return

            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            
            curr.pop()
            dfs(i + 1, curr, total)
        dfs(0, [], 0)
        return res