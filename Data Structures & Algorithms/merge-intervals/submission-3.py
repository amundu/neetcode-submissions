class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if output[-1][1] < curr[0]:
                output.append(curr)
            else:
                output[-1][0] = min(output[-1][0], curr[0])
                output[-1][1] = max(output[-1][1], curr[1])
        return output