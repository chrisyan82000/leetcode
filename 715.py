class RangeModule(object):

     def __init__(self):
        self.stack = []

     def addRange(self, left, right):
        start = bisect.bisect_left(self.stack, left)
        end = bisect.bisect_right(self.stack, right)
        newInterval = []
        if start % 2 == 0: newInterval.append(left)
        if end % 2 == 0: newInterval.append(right)
        self.stack[start:end] = newInterval

     def queryRange(self, left, right):
        start = bisect.bisect_right(self.stack, left)
        end = bisect.bisect_left(self.stack, right)
        return start == end and start % 2 == 1

     def removeRange(self, left, right):
        start = bisect.bisect_left(self.stack, left)
        end = bisect.bisect_right(self.stack, right)
        removedInterval = []
        if start % 2 == 1: removedInterval.append(left)
        if end % 2 == 1: removedInterval.append(right)
        self.stack[start:end] = removedInterval

