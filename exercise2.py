
from exercise1 import emotions

class Person:

    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions

    def __str__(self):
        return "my name is {} and I feel {}".format(self.name, self.emotions)
        


my_person = Person('John', emotions)