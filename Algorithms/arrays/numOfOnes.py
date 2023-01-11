def numOfOnes(n):
    sum = 0 
    while n:
        sum += n % 2
        n = n >> 1
    return sum

num = 0b10000100100001001010010000001
print(numOfOnes(num))