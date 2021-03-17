def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for start,end in intervals:
            if end <= toBeRemoved[0] or start > toBeRemoved[1]:
                res.append([start,end])
            elif start == toBeRemoved[0] and end == toBeRemoved[1]:
                continue
            elif start == toBeRemoved[0] and end < toBeRemoved[1]:
                continue
            elif start == toBeRemoved[0] and end > toBeRemoved[1]:
                res.append([toBeRemoved[1],end])
            elif start >= toBeRemoved[0] and end == toBeRemoved[1]:
                continue
            elif start >= toBeRemoved[0] and end <= toBeRemoved[1]:
                continue
            elif start >= toBeRemoved[0] and end > toBeRemoved[1]:
                res.append([toBeRemoved[1],end])
            elif start < toBeRemoved[0] and end == toBeRemoved[1]:
                res.append([start,toBeRemoved[0]])
            elif start < toBeRemoved[0] and end > toBeRemoved[1]:
                res.append([start,toBeRemoved[0]])
                res.append([toBeRemoved[1],end])
            elif start < toBeRemoved[0] and end < toBeRemoved[1]:
                res.append([start, toBeRemoved[0]])
        return res
