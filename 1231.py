def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """
        left = min(sweetness) # 结果的最小值
        right = sum(sweetness)//(K + 1) # 结果的最大值
        while left <= right:
            mid = (left + right) // 2
            
            cnt = 0 # 用来记录当我分到的巧克力甜度为mid的时候，切的总块数
            tmp = 0 # 当前切的这块巧克力的总甜度
            for sweet in sweetness:
                if (tmp + sweet) > mid:
                    cnt += 1
                    tmp = 0
                else:
                    tmp += sweet
            
            if cnt < K + 1: # 需要切更多块
                right = mid - 1
            else:
                left = mid + 1
        
        return left

