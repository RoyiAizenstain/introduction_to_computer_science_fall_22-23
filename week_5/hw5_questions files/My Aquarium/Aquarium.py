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
                    board[row].append(" ")
    return board


def add_in_place(board, char, x, y):
    board[y][x] = char


def generate_board_str(board_list):
    board_str = ""
    cnt1 = 0
    for row in board_list:
        cnt = 0
        cnt1 += 1
        for col in row:
            cnt += 1
            if col == "":
                board_str += "  "
            else:
                if cnt == len(row):
                    board_str += col
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


def update_position_if_fish(main_corner, height, board):
    x = main_corner[0]
    y = main_corner[1]
    max_height = len(board)
    if max_height - (y + height) <= height:
        y = max_height - 5 - (height - 1) - 1
    return x, y


def is_empty_place(board, x, y):
    if board[y][x] == " ":
        return True
    else:
        return False


def is_available_place_for_list(lst, main_corner, board):
    x = main_corner[0]
    y = main_corner[1]
    lst = lst
    for row in lst:
        for col in row:
            if not is_empty_place(board, x, y):
                return False
            x += 1
        x = main_corner[0]
        y += 1
    return True


def pos_x(animal):
    return animal.x


class Aquarium:
    def __init__(self, aqua_width, aqua_height):
        if not isinstance(aqua_width, int) or not isinstance(aqua_height, int):
            raise InvalidInputException
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
            self.aqua_width) + " and currently in step " + str(self.step) + ", contains the following animals:\n"
        for animal in self.animals:
            aquarium_str += str(animal) + "\n"
        return aquarium_str

    def __repr__(self):
        return generate_board_str(self.board)

    def feed_all(self):
        for animal in self.animals:
            animal.add_food(10)

    def __insert_animal_to_board(self, animal):
        x = animal.x
        y = animal.y
        animal_list = animal.get_animal()
        for row in animal_list:
            for col in row:
                if col != " ":
                    add_in_place(self.board, "*", x, y)
                x += 1
            x = animal.x
            y += 1

    def __delete_animal_from_board(self, animal):
        x = animal.x
        y = animal.y
        animal_list = animal.get_animal()
        for row in animal_list:
            for col in row:
                add_in_place(self.board, "", x, y)
                x += 1
            x = animal.x
            y += 1

    def add_animal(self, name, age, x, y, directionH, directionV, animaltype):
        animal = generate_animal(name, age, x, y, directionH, directionV, animaltype)
        main_corner = [x, y]
        width = animal.width
        height = animal.height
        main_corner[0], main_corner[1] = update_position_if_out(main_corner, width, height, self.board)
        if animaltype in ["shrimp", "ocypode"]:
            main_corner[1] = len(self.board) - 1 - animal.height
        if animaltype in ["molly", "scalar"]:
            main_corner[0], main_corner[1] = update_position_if_fish(main_corner, height, self.board)
        if not is_available_place_for_list(animal.get_animal(), main_corner, self.board):
            raise NotAvailablePlace
        animal.x = main_corner[0]
        animal.y = main_corner[1]
        self.__insert_animal_to_board(animal)
        self.animals.append(animal)

    def __kill_animal(self, animal):
        if animal.starvation():
            self.__delete_animal_from_board(animal)
            self.animals.pop(self.animals.index(animal))
        if animal.die():
            self.__delete_animal_from_board(animal)
            self.animals.pop(self.animals.index(animal))

    def next_step(self):
        self.step += 1
        animals_temp = self.animals.copy()
        self.board = generate_new_board_list(self.aqua_width, self.aqua_height)
        for animal in animals_temp:
            self.__kill_animal(animal)
        crabs_temp = []
        for animal in self.animals:
            if type(animal) is Shrimp:
                crabs_temp.append(animal)
            if type(animal) is Ocypode:
                crabs_temp.append(animal)
        crabs_temp = sorted(crabs_temp, key=pos_x)
        cnt = 0
        for crab in crabs_temp:
            if len(crabs_temp) == cnt + 1:
                break
            crab1 = crab
            crab2 = crabs_temp[cnt + 1]
            if pos_x(crab1) + 8 >= pos_x(crab2):
                if crab1.get_directionH() == 1 and crab2.get_directionH() == 0:
                    crab1.set_directionH(0)
                    crab2.set_directionH(1)
            cnt += 1
        for animal in self.animals:
            if animal.y == 3:
                animal.set_directionV(0)
            if animal.x == 1:
                animal.set_directionH(1)
            if animal.x + animal.width == self.aqua_width - 1:
                animal.set_directionH(0)
            if animal.y + animal.height == self.aqua_height - 5:
                animal.set_directionV(1)
            animal.move()
            self.__insert_animal_to_board(animal)
        for animal in self.animals:
            if self.step % 10 == 0:
                animal.inc_age()
                animal.dec_food()

    def several_steps(self, steps):
        for step in range(steps):
            self.next_step()

