from Animal import Animal
import copy


class Crab(Animal):
    def __init__(self, name, age, food, width, height, x, y, directionH):
        Animal.__init__(self, name, age, food, width, height, x, y, directionH)

    def get_animal(self):
        return self

    def move(self):
        pass


royi = Crab("royi", 120, 120, 4, 4, 4, 4, 4)
print(royi.die())
