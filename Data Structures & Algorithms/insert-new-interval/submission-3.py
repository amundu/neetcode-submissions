class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for i, interval in enumerate(intervals):
            if newInterval[0] > interval[1]:
                output.append(interval)
            elif newInterval[1] < interval[0]:
                output.append(newInterval)
                return output + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        output.append(newInterval)
        return output
