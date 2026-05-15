class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort()
        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if prev[1] < curr[0]:
                output.append(prev)
                prev = curr
            else:
                prev[0] = min(prev[0], curr[0])
                prev[1] = max(prev[1], curr[1])
        output.append(prev)
        return output