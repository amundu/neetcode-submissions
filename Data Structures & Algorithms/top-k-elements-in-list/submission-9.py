class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs_counter = Counter(nums)
        freqs_bucket = [[] for _ in range((len(nums)+1))]

        for n, count in freqs_counter.items():
            freqs_bucket[count].append(n)
        res = []
        for i in range(len(freqs_bucket)-1, -1, -1):
            for n in freqs_bucket[i]:
                res.append(n)
                k -= 1
                if k == 0:
                    return res
                