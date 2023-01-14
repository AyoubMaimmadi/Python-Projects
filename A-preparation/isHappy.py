def isHappy(n):
    visit = set()

    while n not in visit:
        visit.add(n)
        n = sumOfSquares(n)

        if n == 1:
            return True
    
    return False


def sumOfSquares(n):
    output = 0

    while n:
        digit = n % 10
        digit = digit ** 2
        output += digit
        n = n // 10
    return output

print(isHappy(2))