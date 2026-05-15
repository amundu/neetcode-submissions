class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = Counter(tasks)
        max_heap = [-cnt for cnt in mp.values()]
        heapq.heapify(max_heap)
        q = deque()

        cycle = 0

        while max_heap or q:
            cycle += 1
            if max_heap:
                cnt = heapq.heappop(max_heap)
                cnt += 1
                if cnt:
                    q.append((cnt, cycle + n))
            else:
                cycle = q[0][1]
            if q and q[0][1] == cycle:
                cnt, _ = q.popleft()
                heapq.heappush(max_heap, cnt)
        return cycle
            