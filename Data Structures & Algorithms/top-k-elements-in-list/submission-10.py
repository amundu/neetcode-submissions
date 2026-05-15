class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [(e, count) for count, e in Counter(nums).items()]
        return [n for _, n in heapq.nlargest(k, freqs)]