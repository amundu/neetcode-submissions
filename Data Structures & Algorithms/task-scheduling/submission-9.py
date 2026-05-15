class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = Counter(tasks)
        max_heap = [-cnt for cnt in mp.values()]
        heapq.heapify(max_heap)
        q = deque()

        cycle = 0

        while max_heap or q:
            cycle += 1
            if not max_heap:
                cycle = q[0][1]
            else:
                cnt = heapq.heappop(max_heap) + 1
                if cnt: q.append((cnt, cycle + n))
            if q and q[0][1] == cycle:
                heapq.heappush(max_heap, q.popleft()[0])
        return cycle
            