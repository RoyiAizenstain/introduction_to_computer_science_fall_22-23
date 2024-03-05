from unittest import TestCase
from Molly import Molly
from Exceptions import *


class TestMolly(TestCase):
    def setUp(self):
        self.molly = Molly('mymolly', 12, 10, 10, 1, 0)

    def test_init(self):
        self.assertEqual(self.molly.directionH, 1, msg='error in init')
        self.assertEqual(self.molly.directionV, 0, msg='error in init')
        self.assertEqual(0, self.molly.directionV, msg='error in init')
        self.assertEqual(10, self.molly.x, msg='error in init')
        self.assertEqual(10, self.molly.y, msg='error in init')
        self.assertEqual(12, self.molly.age, msg='error in init')
        self.assertEqual("mymolly", self.molly.name, msg='error in init')
        self.assertEqual(3, self.molly.height, msg='error in init')
        self.assertEqual(8, self.molly.width, msg='error in init')
        with self.assertRaises(InvalidInputException):
            Molly('', 12, 10, 10, 1, 0)
        with self.assertRaises(InvalidInputException):
            Molly(4, 12, 10, 10, 1, 0)
        with self.assertRaises(InvalidInputException):
            Molly('mymoly', 122, 10, 10, 1, 0)
        with self.assertRaises(InvalidInputException):
            Molly('mymoly', "12", 10, 10, 1, 0)
        with self.assertRaises(InvalidInputException):
            Molly('mymoly', 12, -1, 10, 1, 0)
        with self.assertRaises(InvalidInputException):
            Molly('mymoly', 12, "", 10, 1, 0)
        with self.assertRaises(InvalidInputException):
            Molly('mymoly', 12, 1, "", 1, 0)
        with self.assertRaises(InvalidInputException):
            Molly('mymoly', 12, 1, -1, 1, 0)
        with self.assertRaises(InvalidInputException):
            Molly('mymoly', 12, 1, 1, 2, 0)
        with self.assertRaises(InvalidInputException):
            Molly('mymoly', 12, 1, 1, "", 0)
        with self.assertRaises(InvalidInputException):
            Molly('mymoly', 12, 1, 1, 1, 2)
        with self.assertRaises(InvalidInputException):
            Molly('mymoly', 12, 1, 1, 1, "")

    def test_str(self):
        self.assertEqual("The molly mymolly is 12 years old and has 10 food.", str(self.molly),
                         msg='error in str')

    def test_repr(self):
        self.assertEqual('*     * * * *  \n* * * * * * * *\n*     * * * *  \n', repr(self.molly),
                         msg='error in repr')

    def test_get_animal(self):
        molly_right = [["*", " ", " ", "*", "*", "*", "*", " "],
                       ["*", "*", "*", "*", "*", "*", "*", "*"],
                       ["*", " ", " ", "*", "*", "*", "*", " "]]
        molly_left = [[" ", "*", "*", "*", "*", " ", " ", "*"],
                      ["*", "*", "*", "*", "*", "*", "*", "*"],
                      [" ", "*", "*", "*", "*", " ", " ", "*"]]
        self.assertEqual(molly_right, self.molly.get_animal(), msg='error in get_animal')
        self.assertNotEqual(molly_left, self.molly.get_animal(), msg='error in get_animal')

    def test_get_position(self):
        self.assertEqual((10, 10), self.molly.get_position(),
                         msg='error in get_position')

    def test_get_size(self):
        self.assertEqual((8, 3), self.molly.get_size(),
                         msg='error in get_size')

    def test_get_directionH(self):
        self.assertEqual(0, self.molly.get_directionV(), msg='error in get_directionH')

    def test_set_directionH(self):
        self.molly.set_directionH(0)
        self.assertEqual(0, self.molly.get_directionH(), msg='error in get_directionH')

    def test_add_food(self):
        self.molly.add_food(10)
        self.assertEqual(20, self.molly.food,
                         msg='error in add_food')

    def test_dec_food(self):
        self.molly.dec_food()
        self.assertEqual(9, self.molly.food,
                         msg='error in dec_food')

    def test_inc_age(self):
        self.molly.inc_age()
        self.assertEqual(10, self.molly.food,
                         msg='error in dec_food')

    def test_starvation(self):
        self.assertEqual(False, self.molly.starvation(),
                         msg='error in starvation')
        self.molly.food = 0
        self.assertEqual(True, self.molly.starvation(),
                         msg='error in starvation')

    def test_die(self):
        self.assertEqual(False, self.molly.die(),
                         msg='error in die')
        self.molly.age = 120
        self.assertEqual(True, self.molly.die(),
                         msg='error in die')

    def test_move(self):
        self.molly.move()
        self.assertEqual(11, self.molly.x, msg='error in move')
        self.assertEqual(11, self.molly.y, msg='error in move')

    def test_get_directionV(self):
        self.assertEqual(0, self.molly.get_directionV(), msg='error in get_directionV')

    def test_set_directionV(self):
        self.molly.set_directionV(1)
        self.assertEqual(1, self.molly.get_directionV(), msg='error in get_directionV')
