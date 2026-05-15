"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        timeline = []
        for interval in intervals:
            timeline.append((interval.start, 1))
            timeline.append((interval.end, -1))
        
        timeline.sort()
        curr_meeting_rooms= max_meeting_rooms = 0
        for event in timeline:
            curr_meeting_rooms += event[1]
            max_meeting_rooms = max(max_meeting_rooms, curr_meeting_rooms)

        return max_meeting_rooms