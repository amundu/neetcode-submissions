class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq = 0
        for n in nums_set:
            if n-1 not in nums_set:
                length = 0
                while n+length in nums_set:
                    length+=1
                max_seq = max(max_seq, length)
        return max_seq
                    