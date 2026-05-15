class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}

        for i, n in enumerate(nums):
            if n in complement:
                return [complement[n], i]
            complement[target - n] = i