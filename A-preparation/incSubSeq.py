# longest increasing subsequence

nums = [1,3,4,5, 6, 0, 1, 2]

def incSubSeq(list):
    LIS = [1] * len(list)

    for i in range(len(list) -1, -1, -1):
        for j in range(i + 1, len(list)):
            if list[i] < list[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS) 

print(incSubSeq(nums))

