class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, H = 0, len(nums)-1

        while L <= H:
            mid = ((H-L)//2)+L
            if nums[mid] < target:
                L = mid+1
            elif nums[mid] > target:
                H = mid - 1
            else:
                return mid
        return -1