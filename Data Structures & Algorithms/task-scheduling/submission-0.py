class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # get count for each task
        counter = Counter(tasks)
        # place count in max heap by making -count
        heap = [-count for count in counter.values()]
        heapq.heapify(heap)
        q = deque()
        cycle = 0
        # while q or heap
        while q or heap:
            if heap:
                pending_count = heapq.heappop(heap) 
                if pending_count + 1 < 0:
                    q.append((cycle+n, pending_count+1))
            if q and q[0][0] == cycle:
                heapq.heappush(heap, q.popleft()[1])
            cycle += 1
        return cycle
        # if heap, pop and place (time+n, count+1) if count +1 less than 0