def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        while len(arr) > 1:
            min_val = min(arr)
            idx = arr.index(min_val)
            if idx> 0 and idx <len (arr) - 1: # of left and right have
                left_val, right_val = arr[idx - 1], arr[idx + 1]
                         elif idx == len (arr) - 1: # There are no left and right
                                 left_val, right_val = arr [idx - 1], 16 # 16 Why? Because the maximum only 15
                         elif idx == 0: # There are no left and right
                left_val, right_val = 16, arr[idx + 1]
                
            res += min(min_val * left_val, min_val * right_val)
                         arr.remove (min_val) # delete the current minimum, it has run out
        return res
