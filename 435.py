class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) == 0:
            return 0
        intervals.sort()
        now = intervals[0][1]
        res = 0
        for i in intervals[1:]:
            if i[0] < now:
                now = min(i[1], now)
                res += 1
            else:
                now = i[1]
        return res

