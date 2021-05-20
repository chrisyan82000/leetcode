def nextGreaterElement(nums1, nums2):
#         if not nums1 or not nums2:
#             return []
#         mapper = {}
#         stack = [nums2[0]]  
#         for i in range(1, len(nums2)):
#             while(stack and nums2[i] > stack[-1]):
#                 mapper[stack.pop()] = nums2[i]
#             stack.append(nums2[i]) 
#         for key in stack:
#             mapper[key] = -1
#         return [mapper[key] for key in nums1]      

