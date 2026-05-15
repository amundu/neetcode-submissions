class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        timeline = self.store[key]
        low, high = 0, len(timeline) - 1
        while low <= high:
            mid = low + (high-low)//2
            prev_pos = mid
            if timestamp < timeline[mid][0]:
                high = mid - 1
            elif timestamp > timeline[mid][0]:
                low = mid + 1
            else:
                return timeline[mid][1]
        if low > 0:
            res = timeline[low-1][1]
        return res
                
        
