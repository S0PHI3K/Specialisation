#Creating Parent Class
class Instruments:
    def __init__(self, type, family, owner):
        self.type = type
        self.family = family
        self.owner = owner

    def info(self):
        print(self.type, self.family, self.owner)

#Creating Child Class which will inherit from parent class
class Location(Instruments):
    pass

#Call of information goes through Location class
num_1 = Location ('Flute', 'Woodwind', 'Sophie')
num_1.info()
