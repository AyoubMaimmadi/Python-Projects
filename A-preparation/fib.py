def fib(n):

    one, two = 0, 1
    arr = []

    for i in range(n):
        arr.append(one)
        temp = one
        one = one + two
        two = temp
    
    return arr

print(fib(18))
