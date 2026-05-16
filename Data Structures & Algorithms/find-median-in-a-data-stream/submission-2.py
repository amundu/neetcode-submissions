class MedianFinder:

    def __init__(self):
        self.n = 0
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        if self.n == 0 or -num >= self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        self.n += 1

        h1, h2 = self.max_heap, self.min_heap
        if len(h1) > len(h2): h1, h2 = h2, h1
        min_half = (self.n//2)-1
        if len(h1) == min_half:
            heapq.heappush(h1, -heapq.heappop(h2))

    def findMedian(self) -> float:
        print(self.max_heap, self.min_heap)
        if self.n == 0: return 0.0
        if self.n % 2:
            if len(self.max_heap) >= len(self.min_heap):
                return -self.max_heap[0]
            else:
                return self.min_heap[0]
        return (-self.max_heap[0] + self.min_heap[0])/2
        
        