# Generators are like itterators, but they don't store data
# yield

import sys

def mygenerator(n): 
    for x in range(n):
        yield x

values = mygenerator(100)
print(sys.getsizeof(values))


# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

for x in values:
    print(f'Printed value: {x}')