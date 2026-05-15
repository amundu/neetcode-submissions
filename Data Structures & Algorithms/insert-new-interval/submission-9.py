class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for i, interval in enumerate(intervals):
            new_start, new_end = newInterval
            curr_start, curr_end = interval
            # if it's after 
            if new_start > curr_end:
                output.append(interval)
            # before
            elif new_end < curr_start:
                output.append(newInterval)
                return output + intervals[i:]
            else:
                newInterval[0] = min(new_start, curr_start)
                newInterval[1] = max(new_end, curr_end)
        output.append(newInterval)
        return output
