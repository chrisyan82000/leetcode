class TreeNode(object):
 def __init__(self, val=0, left=None, right=None):
 self.val = val
 self.left = left
 self.right = right
def invertTree(root): 
 if root is not None:
 root.left, root.right = invertTree(root.right),invertTree(root.left)
 return root
