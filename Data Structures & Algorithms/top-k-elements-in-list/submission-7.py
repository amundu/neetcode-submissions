class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [n for n, freq in heapq.nlargest(k, counter.items(), key=lambda e: e[1])]