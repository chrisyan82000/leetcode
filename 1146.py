class SnapshotArray:
    def __init__(self, n):
        self.data = [[[-1, 0]] for _ in range(n)]
        self.snap_id = 0

    def set(self, index, val):
        self.data[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        i = bisect.bisect_right(self.data[index], [snap_id, float("inf")]) - 1
        return self.data[index][i][1]
