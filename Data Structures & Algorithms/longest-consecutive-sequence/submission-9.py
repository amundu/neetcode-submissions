class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        distinct_nums = set(nums)
        seen = set()

        for n in distinct_nums:
            if n in seen:
                continue
            offset = 1
            while n + offset in distinct_nums:
                offset += 1
            res = max(res, offset)
            seen.add(n)
        return res