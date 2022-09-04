from abc import ABC, abstractmethod

class Instruments(ABC):

    @abstractmethod
    def family(self):
        pass

class Music(Instruments):

    def family(self):
        print('There are 4 families of instruments in the orchestra')

music = Music()
music.family()
