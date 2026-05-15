class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        sums = set()
        sums.add(0)
        target = total // 2

        for n in nums:
            for k in list(sums):
                sums.add(k + n)
            if target in sums: return True
        return False