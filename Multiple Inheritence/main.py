class vehical: 
    speed = 0
    def drive(self, speed):
        self.speed = speed
        print('Driving')

    def stop(self):
        self.speed = 0
        print('Stopped')

    def display(self):
        print(f'Driving at {self.speed} speed')

# Freezer class
class Freezer:
    temp = 0
    def freeze(self, temp):
        self.temp = temp
        print('Freezing')

    def display(self):
        print(f'Freezing at {self.temp} temp')

class Freezertruck(vehical, Freezer):
    def display(self):
        print(f'is a freezer: {issubclass(Freezertruck, Freezer)}')
        print(f'is a vehical: {issubclass(Freezertruck, vehical)}')

        # super(vehical, self).display() # works because of Method Resolution Order(MRO)
        # super(Freezer, self).display() # Fails because of Method Resolution Order(MRO)

        Freezer.display(self)
        vehical.display(self)


t = Freezertruck()
t.drive(50)
t.freeze(-30)
print('-'*20)
t.display()