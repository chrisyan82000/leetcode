def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        # Initialize double pointer and sum
        i = j = 0
        sum1 = sum2 = 0
        # Start traversal
        while i < n1 and j < n2:
            # The small pointer goes backward and updates the corresponding sum
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            # When encountering a cross, use a larger value and update both
            else:
                sum1 = sum2 = max(sum1,sum2) + nums1[i]
                i += 1
                j += 1
        # One pointer came to the end first, update the other
        if i < n1:
            sum1 += sum(nums1[i:])
        if j < n2:
            sum2 += sum(nums2[j:])
        # Return the larger value in sum, modulo
        return max(sum1,sum2) % (10**9+7)
