class TreeNode(object):
 def __init__(self, val=0, left=None, right=None):
 self.val = val
 self.left = left
 self.right = right
def InOrderTraversal(root,output):
 if root == None:
 return
 else:
 InOrderTraversal(root.left,output)
 output.append(root.val)
 InOrderTraversal(root.right,output)
def getMinimumDifference(root):
 output = []
 InOrderTraversal(root,output)
 min_abs = float('inf')
 for i in range(1,len(output)):
 min_abs= min(min_abs, output[i] -output[i-1])
 return min_abs 
root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
print(getMinimumDifference(root))
