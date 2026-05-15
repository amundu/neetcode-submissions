class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(curr: List[List[int]]) -> List[List[int]]:
            if not curr:
                return [[]]
            curr_permutations = []
            curr_number = curr[0]
            for permutation in backtracking(curr[1:]):
                permutation.append(curr_number)
                for i in range(len(permutation)-1, -1, -1):
                    curr_permutations.append(permutation[:])
                    if i >= 1:
                        permutation[i], permutation[i-1] = permutation[i-1], permutation[i]
            print(curr_permutations)
            return curr_permutations
        
        return backtracking(nums)