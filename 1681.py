lass Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxi = (nums[-1] - nums[0] ) * k + 1
        ans = maxi
        n = len(nums)
        pack = n // k
        for i in range(k+1):
            l = self.calc(nums[0:i*pack], i)
            r = self.calc(nums[i*pack:], k-i)
            if l >= 0 and r >= 0:
                res = l + r
                print(i, res)
                ans = min(ans, res)
        
        if ans == maxi: return -1
        return ans
        
    def calc(self, nums: List[int], k: int) -> int:
        if not nums or not k: return 0
        
        c = collections.Counter(nums)
        keys = sorted(c.keys())
        if max(c.values()) > k: return -1
        ans, l, r, s = 0, 0, 0, 0
        pack = len(nums) // k
        n = len(nums)
        pq = []
        for subset in range(k):
            include = []
            size = len(c)
            for i in keys:
                if i not in c: continue
                if k-subset == c[i] or size == pack:
                    include.append(i)
                    c[i] -= 1
                else:
                    size -= 1            
            
            ans += include[-1] - include[0]
            
            for j in include:
                if c[j] == 0:
                    del c[j]
            
        return ans
