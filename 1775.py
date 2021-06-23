 def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # 判断无法使两个数组的和相等的情况
        min1,min2 = len(nums1),len(nums2)
        max1,max2 = 6*min1,6*min2
        if max1 < min2 or max2 < min1: return -1

        # 求出两数组和的差，使nums1，nums2保持在数组和小的数组在前的顺序
        sum1,sum2 = sum(nums1),sum(nums2)
        if sum1 > sum2: nums1,nums2 = nums2,nums1
        diff = abs(sum1-sum2)

        # 使用Counter计算每个值出现的次数
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        res = 0

        # 遍历6 -> 2
        for num in range(6,1,-1):
            # 可供变换的数字，当num为6时是 nums1中1出现的次数 加上 nums2中6出现的次数，每一次变换可以使diff缩减num-1
            avlNum = counter1[6 - num + 1] + counter2[num]
            while diff > 0 and avlNum:
                diff -= (num-1)
                avlNum -= 1
                res += 1
            if diff <= 0: return res
