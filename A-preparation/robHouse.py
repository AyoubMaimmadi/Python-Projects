def robHouse(arr):
    rob1, rob2 = 0, 0

    # [rob1, rob2, n, n+1, ...]
    for n in arr: 
        temp = max(n + rob1,  rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

A = [1, 2, 3, 1]

print(robHouse(A))