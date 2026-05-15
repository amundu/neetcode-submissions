class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x, y in points:
            heapq.heappush(min_heap, (math.sqrt(x**2 + y**2), [x, y]))
            print(min_heap)
        return [e[1] for e in heapq.nsmallest(k, min_heap)]