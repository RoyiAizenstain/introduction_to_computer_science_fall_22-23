from Crab import Crab


class Ocypode(Crab):
    def __init__(self, name, age, x, y, directionH):
        self.height = 4
        Crab.__init__(self, name, age, self.height, x, y, directionH)

    def get_animal(self):
        ocypode = [[" ", "*", " ", " ", " ", "*", " "],
                   [" ", " ", "*", "*", "*", " ", " "],
                   ["*", "*", "*", "*", "*", "*", "*"],
                   ["*", " ", " ", " ", " ", " ", "*"]]

        return ocypode


scalar1 = Ocypode('scalar1', 119, 12, 12, 1)
print(scalar1)
print(repr(scalar1))
scalar1.inc_age()
scalar1.die()
for _ in range(10):
    scalar1.dec_food()
scalar1.starvation()