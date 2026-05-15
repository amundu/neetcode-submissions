class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l: int, r: int) -> int:
            if l == r and nums[l] != target:
                return -1
            m = (r+l)//2
            if target < nums[m]:
                return binary_search(l, m)
            if target > nums[m]:
                return binary_search(m+1, r)
            return m
        
        return binary_search(0, len(nums)-1)