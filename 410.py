def splitArray(self, nums: List[int], m: int) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        start = max(nums)
        end = sum(nums)
        
        while start + 1 < end:
            largest_sum = (start + end) // 2
            if self.largest_sum_satisfy_m(nums, m, largest_sum):
                end = largest_sum
            else:
                start = largest_sum
                
        if self.largest_sum_satisfy_m(nums, m, start):
            return start
        
        return end
    
    def largest_sum_satisfy_m(self, nums, m, largest_sum):
        num_of_sub = 0
        current_sum = 0
        
        for num in nums:
            if current_sum + num <= largest_sum:
                current_sum += num
            else:
                num_of_sub += 1
                current_sum = num
        num_of_sub += 1
        
        return num_of_sub <= m
            
