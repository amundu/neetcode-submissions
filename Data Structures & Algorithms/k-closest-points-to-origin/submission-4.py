class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            x, y = point
            distance = (x**2 + y**2)**(1/2)
            heapq.heappush(min_heap, (-distance, point))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [point for _, point in min_heap]