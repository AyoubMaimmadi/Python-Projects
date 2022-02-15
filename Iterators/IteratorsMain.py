# Iter 

people = ['Ayoub', 'Jiji', 'Bella']
i = iter(people)
print(i)
print(next(i))
print(next(i))
print(next(i))

# Iterable class
import random
class Lotto:
    def __init__(self):
        self.max = 5

    def __iter__(self):
        for _ in range(self._max):
            yield random.randrange(0,100)
    
    def setMax(self, value):
        self._max = value

print('~'*20)
lotto = Lotto()
lotto.setMax(10)

for x in lotto:
    print(x)

print('~'*20)
