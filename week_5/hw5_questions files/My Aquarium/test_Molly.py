from unittest import TestCase
from Molly import Molly


class TestMolly(TestCase):
    def setUp(self):
        self.molly = Molly('mymolly', 12, 10, 10, 1, 0)

    def test_init(self):
        self.assertEqual(1, self.molly.get_directionH(), msg='error in init')
        self.assertEqual(0, self.molly.get_directionV(), msg='error in init')
        self.assertEqual((10,10), self.molly.get_position(), msg='error in init')
        self.assertEqual(12, self.molly.age, msg='error in init')
        self.assertEqual("mymolly", self.molly.name, msg='error in init')

    def test_get_animal(self):
        molly_right = [["*", " ", " ", "*", "*", "*", "*", " "],
                       ["*", "*", "*", "*", "*", "*", "*", "*"],
                       ["*", " ", " ", "*", "*", "*", "*", " "]]
        molly_left = [[" ", "*", "*", "*", "*", " ", " ", "*"],
                      ["*", "*", "*", "*", "*", "*", "*", "*"],
                      [" ", "*", "*", "*", "*", " ", " ", "*"]]
        self.assertEqual(molly_right, self.molly.get_animal(), msg='error in get_animal')
        self.assertNotEqual(molly_left, self.molly.get_animal(), msg='error in get_animal')