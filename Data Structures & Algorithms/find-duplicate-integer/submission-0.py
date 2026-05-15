class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        prev_values = set()

        for n in nums:
            if n in prev_values:
                return n
            prev_values.add(n)