def subarraySum(self, nums: List[int], k: int) -> int:
        counter = collections.Counter()
        res, currSum = 0, 0
        for i in nums:
            currSum += i
            if currSum == k:
                res += 1
            if counter[currSum-k]:
                res += counter[currSum-k]
            counter[currSum] += 1
        return res
