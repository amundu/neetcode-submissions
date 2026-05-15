class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = [[]]

        for n in nums:
            new_permutations = []
            for p in permutations:
                for i in range(len(p) + 1):
                    new_p = p[:]
                    new_p.insert(i, n)
                    new_permutations.append(new_p)
            permutations = new_permutations
        return permutations