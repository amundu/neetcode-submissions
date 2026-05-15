class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        counter = Counter(nums)
        freqs = [[] for _ in range(len(nums)+1)]
        for n, i in counter.items():
            freqs[i].append(n)
        
        res = []
        for i in range(len(freqs)-1, 0, -1):
            while freqs[i] and k > 0:
                res.append(freqs[i].pop())
                k-=1
        return res
            