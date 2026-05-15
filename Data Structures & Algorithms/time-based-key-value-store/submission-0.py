class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list) # key: [(timestamp, value)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        events = self.hash_map[key]
        res = ""

        l, r = 0, len(events)-1
        print(events)

        while l <= r:
            print(l,r)
            m = (l+r)//2
            (e_timestamp, e_value) = events[m]

            if e_timestamp == timestamp:
                return e_value

            if timestamp < e_timestamp:
                r = m - 1
            else:
                l = m + 1

        if l > 0:
            res = events[l-1][1]
        return res