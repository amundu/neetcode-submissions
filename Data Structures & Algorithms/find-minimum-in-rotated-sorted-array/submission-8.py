class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        while low <= high:
            mid = low + (high-low)//2
            print(nums[mid], low, high, mid)
            if nums[mid] <= nums[mid-1]:
                return nums[mid]
            if nums[mid] <= nums[high]:
                high = mid - 1
            else:
                low = mid + 1