def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        size = len(intervals)
        if size<=1: return size
        sorted_intervals = sorted(intervals)
        rooms=[[sorted_intervals[0][1]]]
        for i in range(1,size):
            booked = False
            for room in rooms:
                if sorted_intervals[i][0]>=room[-1]:
                    room.append(sorted_intervals[i][1])
                    booked = True
                    break
            if not booked:rooms.append([sorted_intervals[i][1]])
        return len(rooms)
