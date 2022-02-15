# Filter(func, itarables)
# returnes true if matches the filter 
# Sub range 
from math import isnan
import random
v = []
for x in range(10):
    v.append(random.randrange(100))
print(v)

def lower(val):
    if val < 50: 
        return True
    else:
        return False
    
f = filter(lower, v)
print(f'Less than 50: {list(f)}')

# Filter types
class Animal: 
    name = ''
    def __init__(self, name):
        self.name = name

class Cat(Animal): 
    def __init__(self, name):
        super().__init__('bella')
    
class Dog(Animal): 
    def __init__(self, name):
        super().__init__('griwa')

animals = []
for x in range(10):
    name = 'Animal ' + str(x)
    if (x % 2) == 0:
        # Even nums
        animals.append(Cat(name))
    else:
        # Odd nums
        animals.append(Dog(name))

print(animals)

for a in animals:
    print(f'Animal: {a.name}')

def cats(value):
    return isinstance(value, Cat)
    
def dogs(value):
    return isinstance(value, Dog)

for c in list(filter(cats,animals)):
    print(f'Cat: {c.name}')

for d in list(filter(dogs,animals)):
    print(f'Dog: {d.name}')