 def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        res = prev = 0
        for _, r in intervals:
            if r > prev:
                res += 1    
                prev = r
        return res
