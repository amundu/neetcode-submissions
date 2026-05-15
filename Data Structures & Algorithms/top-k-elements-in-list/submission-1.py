class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = Counter(nums)

        freqs = []
        for i in range(len(nums)+1):
            freqs.append([])

        for e, i in counter.items():
            freqs[i].append(e)
        
        for i in range(len(freqs) - 1, 0, -1):
            if len(freqs[i]) == 0:
                continue
            
            for n in freqs[i]:
                res.append(n)
                k -= 1
                if k == 0:
                    break
            if k == 0:
                break
        
        return res