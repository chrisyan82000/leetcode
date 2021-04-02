def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        res = 0
        while l <= r:
            m = (l + r) // 2
            tot = sum((x - 1) // m + 1 for x in nums)
            if tot <= threshold:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
