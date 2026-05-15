class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = Counter(tasks)
        q = [(0, -k, task) for task, k in mp.items()]
        heapq.heapify(q)

        cycle = 0

        while q:
            if q[0][0] <= 0:
                _, k, task = heapq.heappop(q)
                k += 1
                if k < 0:
                    heapq.heappush(q, (n + 1, k, task))
            q = [(max(0, c - 1), k, task) for c, k, task in q]
            heapq.heapify(q)
            cycle += 1
        return cycle
            