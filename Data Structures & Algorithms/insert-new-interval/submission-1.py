class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # look for newInterval's place by start time order and insert it
        pos = 0
        for i, interval in enumerate(intervals):
            if newInterval[0] <= interval[0]:
                 break
            pos += 1
        intervals.insert(pos, newInterval)
        i = 1
        while i < len(intervals):
            if intervals[i-1][0] <= intervals[i][0] <= intervals[i-1][1]:
                print(i, intervals)
                intervals[i-1] = self.merge(intervals[i-1], intervals[i])
                intervals.pop(i)
                i -= 1
            i += 1
        return intervals

    def merge(self, interval_1, interval_2):
        start_1, end_1 = interval_1
        start_2, end_2 = interval_2
        res = [min(start_1, start_2), max(end_1, end_2)]
        return res
