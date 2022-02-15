def logged(func):
    def inner(*args, **kwargs):
        val = func(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = func.__name__
            print(f'{fname} returned value {val}')
            f.write(f'{fname} returned value {val}\n')
        return val
    return inner

@logged
def add(x, y):
    return x + y

print(add(10,90))
print(add(100,900))