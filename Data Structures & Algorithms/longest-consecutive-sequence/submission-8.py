class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        nums_set = set(nums)
        for n in nums_set:
            if n-1 in nums_set:
                continue
            i = n
            while i in nums_set:
                i += 1
            longest_seq = max(longest_seq, i-n)
        return longest_seq