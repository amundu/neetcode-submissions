class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        prev_values = set()

        for n in nums:
            prev_values.add(n)
        
        longest_seq = 0
        for n in prev_values:
            if n - 1 in prev_values:
                continue
            
            curr_seq = 1
            next_val = n + 1
            while next_val in prev_values:
                curr_seq += 1
                next_val += 1
            
            if curr_seq > longest_seq:
                longest_seq = curr_seq
        
        return longest_seq