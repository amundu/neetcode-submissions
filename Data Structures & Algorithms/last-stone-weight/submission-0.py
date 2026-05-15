class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)

        while max_heap:
            if len(max_heap) == 1:
                return -max_heap[0]
            first, second = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            new_weight = abs(first-second)
            if new_weight > 0:
                heapq.heappush(max_heap, -new_weight)
        return 0