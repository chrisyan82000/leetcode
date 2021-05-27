 def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
   
        
        posi_len = 0
        nega_len = 0
        ans = 0
        
        for num in nums:
            if num==0:
                posi_len=nega_len = 0
            elif num<0:
                posi_len,nega_len = nega_len,posi_len
                nega_len += 1
                if posi_len>0:
                    posi_len += 1 
            else:
                posi_len += 1
                if nega_len>0:
                    nega_len += 1
            ans = max(ans,posi_len)
        
        return ans

