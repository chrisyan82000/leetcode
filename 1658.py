def minOperations(self, nums: List[int], x: int) -> int:
        val = sum(nums)
        if x > val: return -1   # Even use all nums can't subtract x to zero
        elif x == val: return len(nums)   # Need all nums to complete mission (shortcut)
        
        # left for left bound, right for right bound
        nums.append(0)   # For the case no use right part
        ret, left, right, length = 100000, 0, 0, len(nums)
        while right < length:
            if val > x:   # Too much, move right
                val -= nums[right]
                right += 1
            elif val < x:   # Too less, move left
                val += nums[left]
                left += 1
            else:   # PERFECT, move both
                ret = min(ret, length+left-right-1)
                val = val + nums[left] - nums[right]
                left += 1
                right += 1
        return ret if ret != 100000 else -1
