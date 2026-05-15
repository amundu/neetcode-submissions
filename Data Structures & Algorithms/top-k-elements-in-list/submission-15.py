class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        nums_counter = Counter(nums)

        freqs = [[] for n in range(len(nums)+1)] 
        for n, freq in nums_counter.items():
            freqs[freq].append(n)
        
        for i in range(len(freqs)-1, -1, -1):
            while freqs[i]:
                res.append(freqs[i].pop())
                k -= 1
                if k == 0:
                    return res
