class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        self.k = k
        self.min_heap.sort()

    def add(self, val: int) -> int:
        self.min_heap.append(val)
        for i in range(len(self.min_heap)-1, 0, -1):
            if self.min_heap[i-1] > self.min_heap[i]:
                self.min_heap[i], self.min_heap[i-1] = self.min_heap[i-1], self.min_heap[i]
        return self.min_heap[-self.k]
        
