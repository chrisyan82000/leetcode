findLengthOfShortestSubarray(self, arr):
        
        n = len(arr)
        l,r = 0,n-1
        while l < r and arr[l]<=arr[l+1]:
            l += 1
        while l < r and arr[r-1]<=arr[r]:
            r -= 1
        if l == r:
            return 0
        # print(l,r)
        ret = min(n-l-1,r)
        i,j = 0,r
        while i <= l and j < n:
            if arr[i] <= arr[j]:
                ret = min(ret,j-i-1)
                i += 1
            else:
                j += 1
        return ret

