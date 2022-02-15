# Test class
class person:
    # weak private 
    # We want to use it internally, not in the outside world of this class
    _name = 'No name' # Let's you access it and change it without a function (BAD)
    def setName(self, name):
        self._name = name
        print(f'Setting name to: {self._name}')

    # Strong private
    # We can only see it in the internal class we can't access it outside bc of __
    def __think(self):
        print('Thinking to myself')

    def work(self):
        self.__think()

    # Before and After 
    def __init__(self):
        print('Constructor')

    def __call__(self):
        print('Call someone')


class Child(person):
    def testDouble(self):
        self.__think(self)
