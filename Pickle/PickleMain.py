import pickle

def outline(func):
    def inner(*args, **kwargs):
        print('~'*25)
        print(f'Function: {func.__name__}')
        func(*args, **kwargs)
        print('~'*25) 
    return inner

# Simple class
class Cat:
    def __init__(self, name, age, info):
        self._name = name 
        self._age = age
        self._info = info

    @outline
    def display(self, msg = ''):
        print(msg)
        print(f'{self._name} is a {self._age} years old')
        for k, v in self._info.items():
            print(f'{k} = {v}')

Bella = Cat('Bella', 2, dict(color='White', weight=10, loves='cuddling'))
Bella.display('Testing')

# Serialize

sc = pickle.dumps(Bella) # dumps ends with 's' so its for 'Strings'
print(sc)

with open('cat.txt', 'wb') as f:
    pickle.dump(Bella, f)

# Deserialize
mycat = pickle.loads(sc)
print('From string')
mycat.display('from string')

with open('cat.txt', 'rb') as f:
    diskcat = pickle.load(f)
diskcat.display('from disk')

print(mycat)
print(diskcat)