class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        nums_counter = Counter(nums)
        return [v for k, v in heapq.nlargest(k,  [(v, k) for k, v in nums_counter.items()])]