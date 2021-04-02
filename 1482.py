def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def check(day):
            arr = [1 if x<=day else 0 for x in bloomDay]
            formed = 0
            tmp = 0
            for num in arr:
                if num:
                    tmp += 1
                    if tmp==k:
                        formed += 1
                        tmp = 0
                else:
                    tmp = 0
            
            return formed>=m
        
        lo = min(bloomDay)
        hi = max(bloomDay)+1
        
        while lo+1<hi:
            mid = lo + (hi-lo)//2
            if check(mid):
                hi = mid
            else:
                lo = mid
        
        if check(lo):
            return lo
        else:
            if hi==max(bloomDay)+1:
                return -1
            else:
                return hi
