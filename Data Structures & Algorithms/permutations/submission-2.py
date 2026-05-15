class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def dfs(options):
            if not options:
                res.append(path[::])
                return
            for i, n in enumerate(options):
                exclude_curr = options[:i] + options[i+1:]
                path.append(n)
                dfs(exclude_curr)
                path.pop()

        dfs(nums)
        return res