class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries_copy = sorted(queries)
        intervals.sort()

        min_heap = [] # (size, end_index)
        i = 0
        query_to_res = defaultdict(int)
        for query in queries_copy:
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            while i < len(intervals) and query >= intervals[i][0]:
                if intervals[i][0] <= query <= intervals[i][1]:
                    heapq.heappush(min_heap, (intervals[i][1]-intervals[i][0]+1, intervals[i][1]))
                i += 1
            query_to_res[query] = (min_heap[0][0] if min_heap else -1)
        return [query_to_res[query] for query in queries]