def reverse_integer(n):
    return int(str(n)[::-1])

def rev(n):
    reversed_num = 0
    is_negative = n < 0
    if is_negative:
        n = -n
    while n > 0:
        reversed_num = reversed_num*10 + n%10
        n = n // 10
    if is_negative:
        reversed_num = -reversed_num
    return reversed_num

        

print(reverse_integer(123)) # Output: 321
print(rev(123)) # Output: 321

