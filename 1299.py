def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(arr)
        answer[-1] = -1
        for i in range(len(arr)-2, -1, -1):
          answer[i] = max([answer[i+1], arr[i+1]]) 
        return answer

