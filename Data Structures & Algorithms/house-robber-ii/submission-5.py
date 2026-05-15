class Solution:
    def rob(self, nums: List[int]) -> int:
        cache1 = [-1] * len(nums)
        cache2 = [-1] * len(nums)
        n = len(nums)
        
        def decision(i, n, cache):
            if i >= n:
                return 0
            if cache[i] != -1: return cache[i]
            cache[i] = max(decision(i+1, n, cache), nums[i] + decision(i+2, n, cache))
            return cache[i]
        decision(0, n-1, cache1)
        decision(1, n, cache2)
        return max(cache1[0], cache2[1]) if n > 1 else nums[0]