class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Add elements to set
        nums_set = set(nums)
        res = 0
        # look for the beginnings of sequences 
        # go through each element in set checking if n -1 is in the set
        for n in nums_set:
            # if it's there then we skip
            if n - 1 in nums_set:
                continue
            # otherwise it's a beginning of a sequence
            # We start incrementing by 1 the beginning and check if that next n exists
            curr_length = 1
            while n + 1 in nums_set:
                n += 1
                curr_length += 1
            res = max(res, curr_length)
        return res
        