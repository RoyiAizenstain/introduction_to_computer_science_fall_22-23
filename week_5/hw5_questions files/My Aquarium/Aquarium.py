from Exceptions import *
from Scalar import Scalar
from Molly import Molly


def generate_board_list(width, height):
    board = []
    for row in range(height):
        board.append([])
        for col in range(width):
            if (col == 0 or col == width - 1) and row != height - 1:
                board[row].append("|")
            else:
                if row == 2:
                    board[row].append("~")
                elif row == height - 1 and col == 0:
                    board[row].append("\\")
                elif row == height - 1 and col == width - 1:
                    board[row].append("/")
                elif row == height - 1:
                    board[row].append("_")
                else:
                    board[row].append("")
    return board


def generate_board_str(board_list):
    board_str = ""
    for row in board_list:
        for col in row:
            if col == "":
                board_str += "  "
            else:
                board_str += col + " "
        board_str += "\n"
    return board_str


class Aquarium:
    def __init__(self, aqua_width=40, aqua_height=25):
        if aqua_height < 25:
            raise TooSmallAquariumSize
        if aqua_width < 40:
            raise TooSmallAquariumSize
        self.step = 0
        self.animals = []
        self.aqua_width = aqua_width
        self.aqua_height = aqua_height
        self.board = generate_board_list(aqua_width, aqua_height)

    def __str__(self):
        aquarium_str = "The aquarium, sized " + str(self.aqua_height) + "/" + str(
            self.aqua_width) + " and currently in " + str(self.step) + " step, contains the following animals:"
        for animal in self.animals:
            aquarium_str += "\n" + str(animal)
        return aquarium_str

    def __repr__(self):
        return generate_board_str(self.board)

    def feed_all(self):
        for animal in self.animals:
            animal.add_food(10)


acc = Aquarium(40, 50)
acc.feed_all()
print(repr(acc))
print(str(acc))
