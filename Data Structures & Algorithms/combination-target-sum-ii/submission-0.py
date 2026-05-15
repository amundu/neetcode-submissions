class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start: int, combination: List[int], total: int) -> None:
            if total == target:
                res.append(combination.copy())
                return
            if total > target or start == len(candidates):
                return 
            
            combination.append(candidates[start])
            backtrack(start+1, combination, total + candidates[start])
            combination.pop()
            while start+1 < len(candidates) and candidates[start] == candidates[start+1]:
                start += 1
            backtrack(start+1, combination, total)
        
        backtrack(0, [], 0)
        return res
