class Woodwind:
    def instrument(self):
        print('Flute')

class Brass:
    def instrument(self):
        print('Trumpet')

class Strings:
    def instrument(self):
        print('Cello')

class Percussion:
    def instrument(self):
        print('Triangle')

def Music(play):
    play.instrument()

Sophie = Woodwind()
Chris = Percussion()
Amelia = Strings ()
Daisy = Brass()

Music(Sophie)
Music(Chris)
Music(Amelia)
Music(Daisy)
