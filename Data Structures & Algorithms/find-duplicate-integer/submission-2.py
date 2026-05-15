class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n == 'x':
                continue
            curr = n
            while curr != 'x':
                if nums[curr] == 'x':
                    return curr
                tmp = nums[curr]
                nums[curr] = 'x'
                curr = tmp