class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        nums_set = set(nums)
        
        for n in nums_set:
            if n - 1 in nums_set:
                continue
            
            curr_len = 1
            while n + curr_len in nums_set:
                curr_len += 1
            longest_seq = max(longest_seq, curr_len)
        return longest_seq