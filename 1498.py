def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        l = 10**9+7
        s, e = 0, len(nums)
        nums.sort()        
        def helper(s,e,t):
            while s < e-1:
                m = (s+e)//2
                if nums[m]>t:
                    e = m
                else:
                    s = m
            return e
            
        while s<e:
            if 2*nums[s]>target: return res
            e = helper(s, e, target-nums[s])
            res = (res + 1<<(e-s-1)) % l
            s += 1
