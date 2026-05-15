class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}
        for i, n in enumerate(nums):
            if n in remainder:
                return [remainder[n], i]
            remainder[target-n] = i
