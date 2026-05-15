class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        output = []
        for query in queries:
            length = float('inf')
            for start, end in intervals:
                if start <= query <= end:
                    length = min(length, end-start+1)
            output.append(length if length != float('inf') else -1)
        return output