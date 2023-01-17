def two_sum(array, target):
    dic = {}
    for i, num in enumerate(array):
        if num in dic:
            return dic[num], i
        else:
            dic[target - num] = i
    return None


def twoSum(arr, target):
    
    prevMap = {}

    for i, n in enumerate(arr):
        diff = target - n
        if diff in prevMap: 
            return [prevMap[diff], i]
        prevMap[n] = i  # for the value n its index is i
    return  


def twoSum2(arr, target): 
    
    l, r = 0, len(arr)-1

    while l < r: 
        if arr[l] + arr[r] > target:
            r -= 1
        elif arr[l] + arr[r] < target:
            l += 1
        else: 
            return [l, r]


A = [1, 2, 3, 5, 7]
print(twoSum2(A, 5))
    

arr = [1,2,5,5,3,4,9]
print(twoSum(arr, 8))
print(str(two_sum(arr,8)))