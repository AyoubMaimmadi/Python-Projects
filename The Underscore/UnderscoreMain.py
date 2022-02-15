# _Single
# __Double
# __Before
# After__
# __Both__

# Skipping 
for _ in range(5):
    print('Hello!')
 
# Test class
from person import *

# Before (Single)
# Internam use only, called the weak private
p = person()
p.setName('Ayoub')
print(f'Weak private {p._name}')
p._name = 'NOOOOOO'
print(f'Weak private {p._name}')

# Before (Single)
# Internam use only, avoid conflict in subclass
# and tells python to rewrite the name (Mangling)
p = person()
p.work()
#p.__think()  can't access __think() 
c = Child()
#c.testDouble() can't access __think() 


# After__ (Any)
# Helps avoid naming conflicts with key words
# We can use the key words + __ without generating an error
class_ = person()
print(class_)
class__ = person()
print(class__)

# Before and After __main__ 
# Considered special to python, like the init and main function
p = person()
p.__call__()

