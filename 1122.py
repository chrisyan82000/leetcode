def relatve(arr1,arr2):
 res = []
 for a in arr2:
 for i, b in enumerate(arr1):
 if a == b:
 res.append(arr1[i]) 
 res = res + sorted([a for a in arr1 if a not in arr2]) 
 return res
