from Animal import Animal
import copy


class Crab(Animal):
    def __init__(self, name, age, food, width, height, x, y):
        Animal.__init__(self, name, age, food, width, height, x, y)

    def get_animal(self):
        return self

    def move(self):
        pass

    def die(self):
        pass


royi = Crab("royi", 4, 0, 4, 4, 4, 4)
royi.starvation()
print(royi)
