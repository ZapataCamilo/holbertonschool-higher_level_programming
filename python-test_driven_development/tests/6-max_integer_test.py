#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """To check the code"""

    def test_element(self):
        """If is one element"""

        element = [2]
        self.assertEqual(max_integer(element), 2)
    
    def test_str(self):
        """If is a string"""

        string = 'Hola'
        self.assertEqual(max_integer(string), 'o')
    
    def test_float(self):
        """If is a float"""
        fl = [3.4, 5.78, 8.12, 10.13]
        self.assertEqual(max_integer(fl), 10.13)

    def test_order_list(self):
        """"It is an ordered list"""

        order = [1, 2, 3, 4, 5, 6, 7, 8 ,9]
        self.assertEqual(max_integer(order), 9)

    def test_max_at_bn(self):
        """Max integer at beginnig"""

        bn = [9, 3, 4, 5, 6, 7, 1]
        self.assertEqual(max_integer(bn), 9)

    def test_same_number(self):
        """There are two equal numbers"""

        equal = [9, 3, 4, 5, 6, 4, 1]
        self.assertEqual(max_integer(equal), 9)
    
    def test_list_str(self):
        str_list = ['Name', 'Camilo', 'Colombia']
        self.assertEqual(max_integer(str_list), 'Name')
    
    def test_empty_list(self):
        """If the lisy is empty"""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
