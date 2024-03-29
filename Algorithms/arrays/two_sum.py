"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)
"""
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