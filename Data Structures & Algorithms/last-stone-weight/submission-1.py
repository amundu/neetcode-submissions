class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first, second = heapq.heappop(max_heap), heapq.heappop(max_heap)
            if second > first:
                heapq.heappush(max_heap, first - second)
        
        return -max_heap[0] if max_heap else 0