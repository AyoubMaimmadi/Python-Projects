def maxSubArray(arr): 
    
    maxSub = arr[0]
    curSum = 0

    for n in arr: 
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub

A = [1, 2, 4, 55, 6, 7, -75]
print(maxSubArray(A))
    