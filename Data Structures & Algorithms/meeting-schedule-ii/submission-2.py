"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time_line = []
        for interval in intervals:
            time_line.append((interval.start, 1))
            time_line.append((interval.end, -1))
        time_line.sort()

        
        max_meeting_rooms = 0
        curr_meeting_rooms = 0
        for _, change in time_line:
            curr_meeting_rooms += change
            max_meeting_rooms = max(max_meeting_rooms, curr_meeting_rooms)
        return max_meeting_rooms


