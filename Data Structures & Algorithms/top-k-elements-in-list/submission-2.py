class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = Counter(nums)

        freqs = [[] for i in range(len(nums) + 1)]
        for e, i in counter.items():
            freqs[i].append(e)
        
        for i in range(len(freqs) - 1, 0, -1):
            for n in freqs[i]:
                res.append(n)
                if len(res) == k:
                    return res