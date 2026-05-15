class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for e in counter.values():
            if e > 1:
                return True
        return False