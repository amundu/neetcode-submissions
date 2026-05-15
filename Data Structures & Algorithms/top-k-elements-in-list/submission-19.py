class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(len(nums) + 1)] 
        freqs_counter = Counter(nums)

        for n, freq in freqs_counter.items():
            freqs[freq].append(n)
        res = []

        for i in range(len(freqs)-1, 0, -1):
            for n in freqs[i]:
                res.append(n)
                if len(res) == k:
                    return res