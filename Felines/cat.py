# Inheritance

class Feline:
    # We have to set the name in order to not ruin everything 
    def __init__(self, name):
        self.name = name
        print('Creating a feline')

    def meow(self):
        print(f'{self.name}: meow')

    def setName(self, name):
        print(f'{self} setting name: {name}')
        self.name = name

# inheritence of Lien to Feline functions
# Lion Class 
class lion(Feline):
    def roar(self):
        print(f'{self.name}: roar')

# Lion Class 
class tiger(Feline):
    def __init__(self):
        # super allow us to acces the parent 
        super().__init__('No Name') # We need this 
        # if we dont set name at the paret class
        print('Creating Feline ')
        
    def stalk(self):
        print(f'{self.name}: stalking')
    
    def rename(self, name):
        super().setName(name)

b = Feline('Belluh')
print(b)
b.meow()

l = lion('Leo')
print(l)
l.meow()

t = tiger() # a feline with a different constructor
print(t)
# print(t.name())
t.stalk()
t.rename('KING')
t.meow()
