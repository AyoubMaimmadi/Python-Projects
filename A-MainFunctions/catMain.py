from types import new_class
import cat
from cat import Cat

def test():
    b = Cat('Belluh', 2, 'Mixed')
    g = Cat('Griwa', 1, 'Grey')
    b.description()
    g.description()
    b.hungry()
    b.description()
    b.name = "Ayoub"
    b.age = 3
    b.color = "white"
    g.sleep()
    g.description()
    b.meow()
    b.description()

   

if __name__ == "__main__":
    test()
    
