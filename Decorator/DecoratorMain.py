# from decorator import decorator

# Decorator takes in a function, adds some funcionalities and returns it


# Basic decorator 
# In this exampple we will change the execution order

from typing import OrderedDict


def test_decorator(func):
    print('Before')
    func()
    print('After')

@test_decorator
def do_stuff():
    print('Doing stuff')

# Real decorator 
# In this example we will change the functionality
def makeBold(func):
    def inner():
        print('<b>')
        func()
        print('</b>')
    return inner

@makeBold
def printName():
    print('Ayoub Maimmadi')

printName()



# Decorators with parameters
# This has a defined number of parameters 
def numcheck(func):
    def checkInt(o):
        if isinstance(o, int):
            if o == 0:
                print('Cannot devide by zero')
                return False
            return True
        print(f'{o} is is not a number')
        return False

    def inner(x,y):
        if not checkInt(x) or not checkInt(y):
            return
        return func(x,y)
    return inner 

@numcheck
def divide(a,b):
    print(a / b)

divide(5,3)
divide(10,0)
divide(10,'cat')

# Decorator with unknown num of params
# We want a decorator that can pass params and handle anything
# We also want to chain them together 
# *args, **Kwargs to the rescue

def outline(func):
    def inner(*args, **kwargs): 
        print('~'*25)
        func(*args, **kwargs)
        print('~'*25) 
    return inner

def list_items(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print(f'args = {args}')
        print(f'kwargs = {kwargs}')
        for x in args:
            print(f'args = {x}')
        for k,v in kwargs.items():
            print(f'Key = {k}, value = {v}')
    return inner


@outline
@list_items
def display(msg):
    print(msg)

display('Hello Ayoub!')

@outline
@list_items
def birthday(name = ' ', age = 0,):
    print(f'Happy birthday {name} you are {age} years old')

birthday(name = 'Ayoub', age = 21)