class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        prev_values = set(nums)
        
        longest_seq = 0
        for n in prev_values:
            if n - 1 in prev_values:
                continue
            
            length = 1
            while (n + length) in prev_values:
                length += 1
            
            longest_seq = max(longest_seq, length)
        
        return longest_seq