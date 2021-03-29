def solve(self,nums1,nums2):
        t=defaultdict(int)
        res=0
        for num in nums1:
            t[num*num]+=1
        n=len(nums2)
        for i in range(n):
            for j in range(i+1,n):
                key=nums2[i]*nums2[j] 
                if(key in t):
                    res+=t[key]
        return res
        
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res=0
        res+=self.solve(nums1,nums2)
        res+=self.solve(nums2,nums1)
        return res
