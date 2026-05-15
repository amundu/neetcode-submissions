class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.max_heap = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, val)
        return heapq.nlargest(self.k, self.max_heap)[-1]
