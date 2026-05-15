class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [n for n, _ in heapq.nlargest(k, Counter(nums).items(), key=lambda e: e[1])]