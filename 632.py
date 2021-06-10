def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        v  = list()
        for i in range(len(nums)):
            for num in nums[i]:
                v.append((num, i))
        v.sort()
        l, r, n = 0, 0, len(v)
        d = collections.defaultdict(int)
        k = len(nums)
        cnt = 0
        res = [0, 0]
        diff = float('inf')
        while r < n:
            if d[v[r][1]] == 0:
                cnt += 1
            d[v[r][1]] += 1
            while l <= r and cnt == k:
                if v[r][0] - v[l][0] < diff:
                    diff = v[r][0] - v[l][0]
                    res = [v[l][0], v[r][0]]
                d[v[l][1]] -= 1
                if d[v[l][1]] == 0:
                    del d[v[l][1]]
                    cnt -= 1
                l += 1
            r += 1
        return res
