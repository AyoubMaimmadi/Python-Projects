# Exceptions

def outline(func):
    def inner(*args, **kwargs):
        print('~'*25)
        print(f'Function: {func.__name__}')
        func(*args, **kwargs)
        print('~'*25) 
    return inner

# Try, Except and Finally
@outline
def test_one(x,y):
    try:
        z = x / y
        print(f'Result: {z}')
    except: # Same as catch
        print(f'Somthing went wrong x:{x}, y:{y}')
    finally:
        # Always happens
        # Clean up
        print('Complete')

test_one(5,0)
test_one(5,'cat')
test_one(5,2)

@outline
def test_two(x,y):
    try: # Attemp
        assert(x > 0)
        assert(y > 0)
    except AssertionError as ae: # has to do with assertions we made 
        # Specific
        print(f'Failed to assert x:{x} and y:{y}')
    except Exception as e:
        # Same as catch
        print(f'Somthing went wrong x:{x}, y:{y}, issue: {e}')
    else:
        # Trusted 
        z = x / y
        print(f'Result: {z}')
    finally:
        # Clean up
        print('Complete')

test_two(5,0)
test_two(5,'cat')
test_two(5,2)

# User defined exception and raising 
class CatError(RuntimeError):
    def __init__(self, *args):
        self.args = args

@outline
def test_cats(qty):
    try:
        if not isinstance(qty, int):
            raise TypeError('Must be an int')
        if qty < 9:
            raise CatError('Must own more than 9 cats')
        print(f'You own {qty} cats')
    except Exception as ex:
        print(f'Oups: {ex.args}')
    finally:
        print('Conplete!')

test_cats(3)
test_cats('abc') 
test_cats(10)

