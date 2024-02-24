from Crab import Crab


class Shrimp(Crab):
    def __init__(self, name, age, x, y, directionH):
        self.height = 3
        Crab.__init__(self, name, age, self.height, x, y, directionH)

    def get_animal(self):
        shrimp_left = [["*", " ", "*", " ", " ", " ", " "],
                       [" ", "*", "*", "*", "*", "*", "*"],
                       [" ", " ", "*", " ", "*", " ", " "]]

        shrimp_right = [[" ", " ", " ", " ", "*", " ", "*"],
                        ["*", "*", "*", "*", "*", "*", " "],
                        [" ", " ", "*", " ", "*", " ", " "]]

        if self.directionH == 0:
            return shrimp_left
        else:
            return shrimp_right
