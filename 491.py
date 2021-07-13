class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        num_idx={}
        idx_tmp={}
        for i in range(len(nums)):
            if nums[i] in num_idx:
                start=num_idx[nums[i]]
                idx_tmp[i]=[]
            else:
                start=0
                idx_tmp[i]=[[nums[i]]]
            for j in range(start,i):
                if nums[j]<=nums[i]:
                    for t in idx_tmp[j]:
                        tmp=t[:]
                        tmp.append(nums[i])
                        res.append(tmp)
                        idx_tmp[i].append(tmp)
            num_idx[nums[i]]=i 
        return res
