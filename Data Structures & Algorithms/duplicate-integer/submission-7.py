class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev_vals = set()
        for n in nums:
            if n in prev_vals:
                return True
            prev_vals.add(n)
        return False