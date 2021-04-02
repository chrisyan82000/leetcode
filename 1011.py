def shipWithinDays(self, weights: List[int], D: int) -> int:
        left,right=max(weights),sum(weights)
        while left<right:
            mid,d,current_weight=(left+right)//2,1,0
            for w in weights:
                if w+current_weight>mid:
                    d+=1
                    current_weight=0
                current_weight+=w
            if d>D: left=mid+1
            else: right=mid
        return left
