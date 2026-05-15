class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            prev_start, prev_end = output[-1]
            curr_start, curr_end = intervals[i]

            if curr_start > prev_end:
                output.append(intervals[i])
            else:
                output[-1][0] = min(prev_start, curr_start)
                output[-1][1] = max(prev_end, curr_end)
        return output