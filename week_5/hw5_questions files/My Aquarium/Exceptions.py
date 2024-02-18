class InvalidInputException(Exception):
    pass


class NotAvailablePlace(Exception):
    pass


class TooSmallAquariumSize(Exception):
    pass


class InvalidAnimalType(Exception):
    def __init__(self, animal_type):
        self.animal_type = animal_type

    def __str__(self):
        return "Error: \"" + self.animal_type + "\" is an invalid animal type. The valid animal types are: molly, scalar, ocypode, shrimp."

