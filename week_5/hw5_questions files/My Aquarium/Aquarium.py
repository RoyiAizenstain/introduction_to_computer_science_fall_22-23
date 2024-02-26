from Exceptions import *
from Scalar import Scalar
from Molly import Molly
from Shrimp import Shrimp
from Ocypode import Ocypode


def generate_new_board_list(width, height):
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


def add_in_place(board, char, x, y):
    board[y][x] = char


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


def generate_animal(name, age, x, y, directionH, directionV, animaltype):
    if animaltype not in ["scalar", "molly", "shrimp", "ocypode"]:
        raise InvalidAnimalType(animaltype)
    if animaltype == "scalar":
        return Scalar(name, age, x, y, directionH, directionV)
    if animaltype == "molly":
        return Molly(name, age, x, y, directionH, directionV)
    if animaltype == "shrimp":
        return Shrimp(name, age, x, y, directionH)
    if animaltype == "ocypode":
        return Ocypode(name, age, x, y, directionH)


def update_position_if_out(main_corner, width, height, board):
    update_corner = main_corner
    x = main_corner[0]
    y = main_corner[1]
    max_width = len(board[0])
    max_height = len(board)
    if x < 1:
        x = 1
    if y < 3:
        y = 3
    if x + width - 1 >= max_width:
        all = x + width - max_width
        x = x - (all) - 1
    if y + height - 1 >= max_height:
        all = y + height - max_height
        y = y - (all) - 1
    return x, y


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
        self.board = generate_new_board_list(aqua_width, aqua_height)

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
        self.__insert_animal_to_board(Scalar("A", 4, 15, 8, 1, 1))
        self.__insert_animal_to_board(Molly("A", 4, 1, 3, 0, 1))
        self.__delete_animal_to_board(Molly("A", 4, 1, 3, 0, 1))

    def __insert_animal_to_board(self, animal):
        x = animal.x
        y = animal.y
        animal_list = animal.get_animal()
        for row in animal_list:
            for col in row:
                if col[0] != " ":
                    add_in_place(self.board, col, x, y)
                else:
                    add_in_place(self.board, " ", x, y)
                x += 1
            x = animal.x
            y += 1

    def __delete_animal_to_board(self, animal):
        x = animal.x
        y = animal.y
        animal_list = animal.get_animal()
        for row in animal_list:
            for col in row:
                add_in_place(self.board, " ", x, y)
                x += 1
            x = animal.x
            y += 1

    def add_animal(self, name, age, x, y, directionH, directionV, animaltype):
        animal = generate_animal(name, age, x, y, directionH, directionV, animaltype)
        main_corner = (x, y)
        width = animal.width
        height = animal.height
        animal.x, animal.y = update_position_if_out(main_corner, width, height, self.board)
        if animaltype in ["shrimp", "ocypode"]:
            animal.y = len(self.board) - 1 - animal.height
        if animaltype in ["molly", "scalar"]:
            """need to complete"""
        self.__insert_animal_to_board(animal)
        self.animals.append(animal)
        pass

    def __kill_animal(self, animal):
        pass

    def next_step(self):
        pass

    def several_steps(self, steps):
        pass


acc = Aquarium()
acc.add_animal("r", 2, 1111, 10000, 0, 0, "shrimp")
print(repr(acc))
print(str(acc))
