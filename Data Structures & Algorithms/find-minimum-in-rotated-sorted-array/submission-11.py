class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] >= nums[low]:
                if nums[mid] <= nums[high]:
                    return nums[low]
                else:
                    low = mid + 1
            else:
                high = mid