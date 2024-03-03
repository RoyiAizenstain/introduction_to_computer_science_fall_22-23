from unittest import TestCase
from Molly import Molly
from Exceptions import *


class TestMolly(TestCase):
    def setUp(self):
        self.molly_one = Molly('mymolly1', 12, 10, 10, 1, 0)
        self.molly_two = Molly('mymolly2', 12, 1, 3, 1, 0)
        self.molly_three = Molly('mymolly3', 12, 9, 22, 1, 1)

    def test_init(self):
        self.assertIn(self.molly_one.directionH, [1, 0], msg='error in init')
        self.assertIn(self.molly_one.directionV, [1, 0], msg='error in init')
        self.assertEqual(0, self.molly_one.directionV, msg='error in init')
        self.assertEqual(10, self.molly_one.x, msg='error in init')
        self.assertEqual(10, self.molly_one.y, msg='error in init')
        self.assertEqual(12, self.molly_one.age, msg='error in init')
        self.assertEqual("mymolly1", self.molly_one.name, msg='error in init')

    def test_get_animal(self):
        molly_right = [["*", " ", " ", "*", "*", "*", "*", " "],
                       ["*", "*", "*", "*", "*", "*", "*", "*"],
                       ["*", " ", " ", "*", "*", "*", "*", " "]]
        molly_left = [[" ", "*", "*", "*", "*", " ", " ", "*"],
                      ["*", "*", "*", "*", "*", "*", "*", "*"],
                      [" ", "*", "*", "*", "*", " ", " ", "*"]]
        self.assertEqual(molly_right, self.molly_one.get_animal(), msg='error in get_animal')
        self.assertNotEqual(molly_left, self.molly_one.get_animal(), msg='error in get_animal')

    def test_get_directionV(self):
        self.assertEqual(0, self.molly_one.get_directionV(), msg='error in get_directionV')

    def test_set_directionV(self):
        self.molly_two.set_directionV(1)
        self.assertEqual(1, self.molly_two.get_directionV(), msg='error in get_directionV')

    def test_get_directionH(self):
        self.assertEqual(0, self.molly_one.get_directionV(), msg='error in get_directionH')

    def test_set_directionH(self):
        self.molly_two.set_directionH(1)
        self.assertEqual(1, self.molly_two.get_directionH(), msg='error in get_directionH')

    def test_move(self):
        self.molly_three.move()
        self.assertEqual(10, self.molly_three.x, msg='error in move')
        self.assertEqual(21, self.molly_three.y, msg='error in move')

    def test_str(self):
        self.assertEqual("The molly mymolly3 is 12 years old and has 10 food.", str(self.molly_three),
                         msg='error in str')

    def test_repr(self):
        self.assertEqual('*     * * * *  \n* * * * * * * *\n*     * * * *  \n', repr(self.molly_three),
                         msg='error in repr')

    def test_add_food(self):
        self.molly_three.add_food(10)
        self.assertEqual(20, self.molly_three.food,
                         msg='error in repr')

    def test_dec_food(self):
        self.molly_three.dec_food()
        self.assertEqual(9, self.molly_three.food,
                         msg='error in dec_food')

    def test_inc_age(self):
        self.molly_three.inc_age()
        self.assertEqual(10, self.molly_three.food,
                         msg='error in dec_food')

    def test_get_position(self):
        self.assertEqual((9, 22), self.molly_three.get_position(),
                         msg='error in get_position')

    def test_get_size(self):
        self.assertEqual((8, 3), self.molly_three.get_size(),
                         msg='error in get_size')

    def test_starvation(self):
        self.assertEqual(False, self.molly_three.starvation(),
                         msg='error in starvation')
        self.molly_three.food = 0
        self.assertEqual(True, self.molly_three.starvation(),
                         msg='error in starvation')

    def test_die(self):
        self.assertEqual(False, self.molly_three.die(),
                         msg='error in die')
        self.molly_three.age = 120
        self.assertEqual(True, self.molly_three.die(),
                         msg='error in die')
