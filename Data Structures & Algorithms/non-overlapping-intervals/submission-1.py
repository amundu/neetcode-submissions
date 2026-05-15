class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        output = 0
        intervals.sort()
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                output += 1
                prev_end = min(prev_end, intervals[i][1])
            else:
                prev_end = intervals[i][1]
        return output