class TreeNode(object):
 def __init__(self, val=0, left=None, right=None):
 self.val = val
 self.left =left
 self.right = right
def mergeTree(t1, t2):
 if t1 == None and t2 == None:
 return None
 if t1 == None:
 return t2
 if t2 == None:
 return t1
 val = t1.val + t2.val 
 node = TreeNode(val)
 node.left = mergeTree(t1.left, t2.left)
 node.right = mergeTree(t1.right,t2.right)
 return node
