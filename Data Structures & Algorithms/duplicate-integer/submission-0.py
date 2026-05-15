class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}

        for e in nums:
            if e in duplicates:
                return True
            duplicates[e] = 1
        return False