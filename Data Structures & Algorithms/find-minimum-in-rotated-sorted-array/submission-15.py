class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        while low <= high:
            mid = ((high-low)//2)+low
            if nums[low] <= nums[mid]:
                if nums[low] <= nums[high]:
                    return nums[low]
                low = mid + 1
            else:
                high = mid