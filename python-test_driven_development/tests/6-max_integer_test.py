#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function"""

    # Test: max integer in a list of positive integers
    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    # Test: max integer in a list with mixed positive and negative integers
    def test_mixed_integers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    # Test: max integer in a list with all negative integers
    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    # Test: max integer in a list with a single element
    def test_single_element(self):
        self.assertEqual(max_integer([4]), 4)

    # Test: max integer in an empty list
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    # Test: invalid type (string in the list)
    def test_type_error(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "four"])

if __name__ == '__main__':
    unittest.main()
