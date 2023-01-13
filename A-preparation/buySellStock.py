def buySellStock(arr):

    l, r = 0, 1
    currSum = 0 

    while r < len(arr):
        if arr[l] < arr[r]:
            diff = arr[r] - arr[l]
            currSum = max(currSum, diff)
        else: 
            l = r   
        r += 1
    return currSum


A = [7, 1, 5, 3, 6, 4]
print(buySellStock(A))

