 def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        queue = [root]
        while queue:
            new_queue = []
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            if not new_queue:
                return self.lca(root, queue)
            queue = new_queue
    
    def lca(self, root, nodes):
        if root is None or root in set(nodes):
            return root
        
        left = self.lca(root.left, nodes)
        right = self.lca(root.right, nodes)
        
        return root if left and right else left or right
