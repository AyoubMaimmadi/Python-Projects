class vector:

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)

    # to_string()
    def __repr__(self) -> str:  
        return f'X: {self.x}, Y: {self.y}'

    def __len__(self):
        return 10

    def __call__(self):
        print('Hello, i was called')




v1 = vector(10, 20)
v2 = vector(50, 60)
v3 = v1 + v2

print('v3.x = ' + str(v3.x))
print('v3.y = ' + str(v3.y))
print(v3)

v3()

    