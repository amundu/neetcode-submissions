class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_product = max_product = 1
        res = float('-inf')
        has_zeros_only = True
        for i in range(len(nums)):
            n = nums[i]
            if n != 0: has_zeros_only = False
            if n == 0:
                res = max(res, min_product, max_product)
                min_product = max_product = 1
            min_product, max_product = min(n, min_product * n, max_product * n), max(n, min_product * n, max_product * n)
            res = max(res, min_product, max_product)
        return res if not has_zeros_only else 0