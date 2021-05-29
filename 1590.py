def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        suml=sum(nums)
        ctr=0
        l1=[]
        if suml%p==0:
            return 0
        else:
            rem=suml%p
            if rem in nums:
                return 1
            else:
                nums1=list(filter(lambda  x : x<rem,nums ))
                k=0
                i=2
                while (k!=1):
                    if i<len(nums1):
                        l1=list(combinations(nums1,i))
                        i=i+1
                    else:
                        k=1
                    l2=list(filter(lambda x:sum(x)==rem,l1))
                    if len(l2)>0:
                        k=1
        if len(l2)==0:
            return -1
        else:
            return len(l2[0])

