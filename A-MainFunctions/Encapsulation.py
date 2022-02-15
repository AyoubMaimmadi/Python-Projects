class person: 
    def __init__(self, name, age, gender):
        self.__name = name
        self.age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name
        
    @Name.setter
    def Name(self, name):
        self.__name = name

    @property
    def Gender(self):
        return self.__gender

    @Gender.setter
    def Gender(self, val):
        self.__gender = val

    @staticmethod
    def mymethod() -> str:
        print(f'Fuck you cunt!')

person.mymethod()

p1 = person('Ayoub', 21, 'Male')
# print(p1.name) # We cant do this because of __name
print(p1.Name)
p1.Name = 'Maimmadi'
print(p1.age)
print(p1.Gender)
print(f'Name changed to: {p1.Name}')
p1.mymethod()

