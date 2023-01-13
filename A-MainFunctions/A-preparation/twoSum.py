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
        prevMap[n] = i
    return  



arr = [1,2,5,5,3,4,9]
print(twoSum(arr, 8))
print(str(two_sum(arr,8)))