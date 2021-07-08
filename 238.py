def productExceptSelf(self, nums: List[int]) -> List[int]:        
        #scan from left to i
        for i in range(n):
            output.append(p)
            p = p * nums[i]
        p = 1
        #scan from right to i
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
