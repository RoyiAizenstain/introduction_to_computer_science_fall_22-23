from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, food, width, height):
        self.name = name
        self.age = age
        self.food = food
        self.width = width
        self.height = height
