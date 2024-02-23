from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, width, height, x, y, directionH):
        self.name = name
        self.age = age
        self.food = 10
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.directionH = directionH

    def __str__(self):
        return "The " + type(self).__name__.lower() + " " + self.name + " is " + str(self.age) + " years old and has " + str(
            self.food) + " food."

    def __repr__(self):
        return str(self.get_animal())

    def get_position(self):
        return self.x, self.y

    def get_size(self):
        return self.width, self.height

    def add_food(self, amount):
        self.food += amount

    def dec_food(self, food):
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
