def moveZeroes(self, nums):
 i = 0
 j = 0
 while j < len(nums):
 if nums[j] == 0:
 j += 1
 else:
 nums[i] = nums[j]
 i += 1
 j += 1
 while i < len(nums):
 nums[i] = 0
 i += 1
 Return nums
