class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = Counter(tasks)
        q = [(0, -k) for _, k in mp.items()]
        heapq.heapify(q)

        cycle = 0

        while q:
            if q[0][0] <= 0:
                _, k = heapq.heappop(q)
                k += 1
                if k < 0:
                    heapq.heappush(q, (n + 1, k))
            q = [(max(0, c - 1), k) for c, k in q]
            heapq.heapify(q)
            cycle += 1
        return cycle
            