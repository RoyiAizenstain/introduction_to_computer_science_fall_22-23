from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, food, width, height, x, y):
        self.name = name
        self.age = age
        self.food = food
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "The " + type(self).__name__ + " " + self.name + " is " + str(self.age) + " years old and has " + str(
            self.food) + " food."

    def __repr__(self):
        return str(self.get_animal())

    def get_position(self):
        return self.x, self.y

    def get_size(self):
        return self.width, self.height

    def add_food(self, amount):
        self.food += amount

    def inc_age(self):
        self.age += 1

    def starvation(self):
        if self.food == 0:
            print(str(self.name) + " died at the age of " + str(self.age) + " years because it ran out of food .")
            return True

    @abstractmethod
    def get_animal(self):
        pass
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def die(self):
        pass
