class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        distinct_nums = set(nums)

        for n in distinct_nums:
            if n-1 in distinct_nums:
                continue
            offset = 1
            while n + offset in distinct_nums:
                offset += 1
            res = max(res, offset)
        return res