from Fish import Fish


class Molly(Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        self.height = 3
        Fish.__init__(self, name, age, self.height, x, y, directionH, directionV)

    def get_animal(self):
        molly_left = [[" ", "*", "*", "*", "*", " ", " ", "*"],
                      ["*", "*", "*", "*", "*", "*", "*", "*"],
                      [" ", "*", "*", "*", "*", " ", " ", "*"]]

        molly_right = [["*", " ", " ", "*", "*", "*", "*", " "],
                       ["*", "*", "*", "*", "*", "*", "*", "*"],
                       ["*", " ", " ", "*", "*", "*", "*", " "]]
        if self.directionH == 0:
            return molly_left
        else:
            return molly_right

