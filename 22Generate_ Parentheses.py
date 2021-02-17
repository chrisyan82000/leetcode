def generatePara(n):
    result = []
    helper(result, n, n, '')
    return result
def helper(result,left,right,path):
    if left == 0 and right ==0:
       result.append(path)
       return result 
    if left > 0:
        helper(result, left -1, right, path + '(')
    if left < right :
        helper(result, left, right-1, path + ')')
n=3
print(generatePara(n)
