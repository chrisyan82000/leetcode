if postorder == inorder == []:
            return None
        else:
            rootVal = postorder[-1]
            root = TreeNode(rootVal)
            k = inorder.index(rootVal)
            root.left = buildTree(inorder[:k],postorder[:k])
            root.right = buildTree(inorder[k+1:],postorder[k:-1])
            return root
