from abc import ABC, abstractmethod
from Exceptions import *


class Animal(ABC):
    def __init__(self, name, age, width, height, x, y, directionH):
        if not isinstance(name, str) or name == "":
            raise InvalidInputException
        if not isinstance(age, int) or not (0 <= age < 120):
            raise InvalidInputException
        if not isinstance(x, int) or x < 0:
            raise InvalidInputException
        if not isinstance(y, int) or y < 0:
            raise InvalidInputException
        if not (directionH == 0 or directionH == 1):
            raise InvalidInputException
        self.name = name
        self.age = age
        self.food = 10
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.directionH = directionH

    def __str__(self):
        return "The " + type(self).__name__.lower() + " " + self.name + " is " + str(
            self.age) + " years old and has " + str(
            self.food) + " food."

    def __repr__(self):
        def str_animal(animal_list):  # need to change
            animal_str = ""
            for row in animal_list:
                animal_str += " ".join(row) + "\n"
            return animal_str

        return str_animal(self.get_animal())

    def get_position(self):
        return self.x, self.y

    def get_size(self):
        return self.width, self.height

    def add_food(self, amount):
        self.food += amount

    def dec_food(self):
        self.food -= 1

    def inc_age(self):
        self.age += 1

    def starvation(self):
        if self.food == 0:
            print(str(self.name) + " died at the age of " + str(self.age) + " years because it ran out of food.")
            return True
        return False

    def get_directionH(self):
        return self.directionH

    def set_directionH(self, directionH):
        self.directionH = directionH

    def die(self):
        if self.age == 120:
            print(str(self.name) + " died in a good health.")
            return True
        return False

    @abstractmethod
    def get_animal(self):
        pass

    @abstractmethod
    def move(self):
        pass
