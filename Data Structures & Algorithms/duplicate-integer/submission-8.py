class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev_chars = set()

        for n in nums:
            if n in prev_chars:
                return True
            prev_chars.add(n)
        return False