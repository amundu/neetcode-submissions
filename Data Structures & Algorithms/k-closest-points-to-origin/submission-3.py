class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_distance_to_origin(point: List[int]) -> float:
            return (point[0]**2 + point[1]**2)**1/2
        min_heap = [(get_distance_to_origin(point), point) for point in points]
        heapq.heapify(min_heap)
        print(min_heap)
        return [point for _, point in heapq.nsmallest(k, min_heap)]