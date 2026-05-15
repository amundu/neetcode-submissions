class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        pos = 0
        for i, interval in enumerate(intervals):
            if newInterval[0] <= interval[0]:
                 break
            pos += 1
        intervals.insert(pos, newInterval)
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            if output[-1][0] <= intervals[i][0] <= output[-1][1]:
                output[-1][0], output[-1][1] = self.merge(output[-1], intervals[i])
            else:
                output.append(intervals[i])
        return output

    def merge(self, interval_1, interval_2):
        start_1, end_1 = interval_1
        start_2, end_2 = interval_2
        return [min(start_1, start_2), max(end_1, end_2)]
