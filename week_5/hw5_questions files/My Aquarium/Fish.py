from Animal import Animal
from Exceptions import *
import copy


class Fish(Animal):
    def __init__(self, name, age, height, x, y, directionH, directionV):
        self.width = 8
        Animal.__init__(self, name, age, self.width, height, x, y, directionH)
        if not (directionV == 0 or directionV == 1):
            raise InvalidInputException
        self.directionV = directionV

    def get_directionV(self):
        return self.directionV

    def set_directionV(self, directionV):
        self.directionV = directionV
        pass

    def get_animal(self):
        return self

    def move(self):
        if self.directionH == 0:
            self.x -= 1
        else:
            self.x += 1
        if self.directionV == 0:
            self.y += 1
        else:
            self.y -= 1
