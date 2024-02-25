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
