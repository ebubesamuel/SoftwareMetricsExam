"""This program is to determine the modular function (modf) of an argument"""
import unittest
import math
from wrapper_modf import wrapper


class TestModfMethod(unittest.TestCase):
    """"This class has methods which check the validity of an argument for
    the modf wrapper"""

    def test_wrapper_correct_argument(self):
        """This function checks if the argument are of a valid type"""
        self.assertEqual(wrapper(math.pi), (0.14159265358979312, 3.0))

    def test_wrapper_incorrect_arg(self):
        """This function checks if the arguments are of an invalid type"""
        with self.assertRaises(TypeError):
            wrapper("ebu")

    def test_wrapper_no_arg(self):
        """This function checks if the arguments are of valid type"""
        with self.assertRaises(TypeError):
            wrapper()


if __name__ == '__main__':
    unittest.main()
