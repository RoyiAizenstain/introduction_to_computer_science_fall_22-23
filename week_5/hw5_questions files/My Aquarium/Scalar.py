from Fish import Fish


class Scalar(Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        self.height = 5
        Fish.__init__(self, name, age, self.height, x, y, directionH, directionV)

    def get_animal(self):
        scalar_left = [[" ", " ", "*", "*", "*", "*", "*", "*"],
                       [" ", "*", "*", "*", " ", " ", " ", " "],
                       ["*", "*", "*", "*", "*", "*", " ", " "],
                       [" ", "*", "*", "*", " ", " ", " ", " "],
                       [" ", " ", "*", "*", "*", "*", "*", "*"]]

        scalar_right = [["*", "*", "*", "*", "*", "*", " ", " "],
                        [" ", " ", " ", " ", "*", "*", "*", " "],
                        [" ", " ", "*", "*", "*", "*", "*", "*"],
                        [" ", " ", " ", " ", "*", "*", "*", " "],
                        ["*", "*", "*", "*", "*", "*", " ", " "]]
        if self.directionH == 0:
            return scalar_left
        else:
            return scalar_right
