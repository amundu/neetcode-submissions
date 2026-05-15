class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            nums_sum = numbers[l] + numbers[r]
            if (nums_sum) == target:
                return [l+1, r+1]
            elif nums_sum < target:
                l += 1
            else:
                r -= 1 

