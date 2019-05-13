from exercise1 import emotions

class Person:

    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions


    def how_feeling(self, feeling, rate):
        self.rate = rate
        self.feeling = feeling
        if self.rate == 3:
            print('Im am feeling a high amount of {}'.format(self.feeling))
        elif self.rate == 2:
           print('Im am feeling a medium amount of {}'.format(self.feeling))
        elif self.rate ==1:
            print('Im am feeling a low amount of {}'.format(self.feeling))

    def __str__(self):
        return "my name is {} and I feel {}".format(self.name, self.emotions)
        


my_person = Person('John', emotions)
print(my_person)
my_person.how_feeling('happy', 2)