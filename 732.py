class Node(object):
    def __init__(self, start, end, c):
        self.start = start
        self.end = end
        self.count = c
        self.left = None
        self.right = None

class MyCalendarThree(object):
    def __init__(self):
        self.root = None
        self.maxK = 1

    def book_helper(self, root, start, end, c):
        if root == None:
            return Node(start, end, c)
        if start >= root.end:
            #不能写成return self.boook_helper()，因为要进行树的构建和修改，一定要赋值给root.right
            root.right = self.book_helper(root.right, start, end, c)
        elif end <= root.start:
            root.left = self.book_helper(root.left, start, end, c)
        else:
            intervals = sorted([start, end, root.start, root.end])
            root_l, root_r = root.start, root.end
            root.start, root.end = intervals[1], intervals[2]
            root.left = self.book_helper(root.left, intervals[0], intervals[1], c if start <= root_l else root.count)
            root.right = self.book_helper(root.right, intervals[2], intervals[3], c if end >= root_r else root.count)
            root.count += c
            self.maxK = max(root.count, self.maxK)
        return root

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        self.root = self.book_helper(self.root, start, end, 1)
        return self.maxK


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
