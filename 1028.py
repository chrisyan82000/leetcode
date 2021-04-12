def recoverFromPreorder(self, S: str) -> TreeNode:
        # 第一个辅助函数，给定起始点的index，找结点值
        def detectNum(start):
            ret = 0
            while start < len(S) and "0" <= S[start] <= "9":
                ret = ret * 10 + int(S[start])
                start += 1
            # 返回结点值，以及下一个起始点的index
            return ret, start

        # 第二个辅助函数，给定起始点的index，找结点的深度
        def detectDepth(start):
            ret = 0
            while start < len(S) and S[start] == "-":
                ret += 1
                start += 1
            # 返回深度，以及下一个起始点的index
            return ret, start 

        if not S:
            return None
        
        # 找根结点的结点值
        val, idx = detectNum(0)
        # 结构化根结点
        root = TreeNode(val)
        # 根结点入栈
        stack = [root]

        while idx < len(S):
            # 检测当前结点的深度
            depth, idx = detectDepth(idx)
            # 检测当前结点的结点值
            val, idx = detectNum(idx)
    
            # 如果深度小于栈的深度，不断出栈，使得二者深度相等
            # 这样使得栈顶元素是当前结点的父结点
            while depth < len(stack):
                stack.pop()
            # 把父节点取出来
            parent = stack[-1]
            node = TreeNode(val)
            # 如果父节点无左子树，则放到左子树上
            # 反之，放到右子树上
            if not parent.left:
                parent.left = node
            else:
                parent.right = node
            # 当前点入栈
            stack.append(node)
        
        return root
