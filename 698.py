class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def dfs(index):
            if index==len(nums):
                return len(set(buck))== 1
            for i in range(k):
                print('i=%d'%(i),'index=%d'%(index))
                print(buck[i])
                buck[i] += nums[index]
                print(buck[i])
                if buck[i]<= nsum//k and dfs(index+1):
                    return True
                buck[i] -= nums[index]
                if buck[i]==0:
                    break
            return False
            
        nums.sort(reverse=True)
        nsum = sum(nums)
        if nsum%k != 0:
            return False
        if nums[0] > nsum//k:
            return False
        buck = [0]*k
        return dfs(0)
