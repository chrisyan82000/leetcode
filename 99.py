# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.pre, self.first, self.second = None, None, None
        self.inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        if self.pre and self.pre.val > root.val:
            if not self.first:
                self.first = self.pre
            self.second = root
        self.pre = root
        self.inOrder(root.right)
