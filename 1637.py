def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = [p[0] for p in points]
        points.sort()
        res = float("-inf")
        for i in range(1,len(points)):
            a = points[i]
            b = points[i-1]
            res = max(a-b, res)
        return res
