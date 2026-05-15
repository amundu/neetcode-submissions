class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []

        for i, interval in enumerate(intervals):
            if interval[0] > newInterval[0]:
                intervals.insert(i, newInterval)
                break
        if intervals[-1][0] <= newInterval[0]:
            intervals.append(newInterval)

        res.append(intervals[0])
        print(intervals)
        for i in range(1, len(intervals)):
            prev_start, prev_end = res[-1]
            start, end = intervals[i]
            if start > prev_end:
                res.append([start, end])
            else:
                res[-1][0], res[-1][1] = [min(prev_start, start), max(prev_end, end)]
        
        return res