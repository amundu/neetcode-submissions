class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        nums_set = set(nums)
        for n in nums:
            if n-1 in nums_set:
                continue
            length = 1
            while n + length in nums_set:
                length += 1
            longest_seq = max(longest_seq, length)
        return longest_seq