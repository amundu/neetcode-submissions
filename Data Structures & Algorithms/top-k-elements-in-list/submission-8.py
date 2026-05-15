class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs_map = Counter(nums)
        max_heap = []
        for n, count in freqs_map.items():
            heapq.heappush(max_heap, (-count, n))
        res = []
        for _ in range(k, 0, -1):
            res.append(heapq.heappop(max_heap)[1])
        return res