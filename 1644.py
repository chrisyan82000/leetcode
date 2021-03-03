def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not q or not p:
            return None
        self.count = 0
        res = self.dfs(root, p, q)
        if self.count == 2:
            return res
        return None

    def dfs(self, root, p, q):
        if not root:
            return None

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        if root == p or root == q:
            self.count += 1
            return root

        if left and right:
            return root
        else:
            return left or right
