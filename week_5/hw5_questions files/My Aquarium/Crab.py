from Animal import Animal


class Crab(Animal):
    def __init__(self, name, age, height, x, y, directionH):
        self.width = 7
        Animal.__init__(self, name, age, self.width, height, x, y, directionH)

    def get_animal(self):
        return self

    def move(self):
        if self.directionH == 0:
            self.x -= 1
        else:
            self.x += 1
