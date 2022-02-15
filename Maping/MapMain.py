# map
# Looping without a loop
# Maps functions calls to a collection of items 
# map(func, iterabeles)

people = ['Ayoub', 'Zineb', 'Lina', 'Jiji']

# Old way
counts = []
for x in people:
    counts.append(len(x))
print(f'Old way: {counts}')

# Modern way
print(f'Mapped: {list(map(len,people))}')

# More complex - combine elements

firstnames = ('Apple', 'Chocolate', 'Fudge', 'Pizza')
lastnames = ('Pie', 'Cake', 'Brownie')

def merge(a, b):
    return a + ' ' + b

x = map(merge, firstnames, lastnames)

print(x)
print(list(x))

# Multiple finctions - Combine functions
# Call multiple functions in one map call

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b

def doall(func, num):
    return func(num[0],num[1])

f = (add, sub, mult, div)
v = [[5,3]]
n = list(v) * len(f)
print(f'f:{f}, n:{n}')

m = map(doall, f, n)
print(list(m))