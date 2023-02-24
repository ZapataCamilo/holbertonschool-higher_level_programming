import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_init(self):
        t1 = Rectangle(1, 2)
        t2 = Rectangle(6, 9, 0, 0 ,12)
        with self.assertRaises(TypeError):
            Rectangle("string")
            Rectangle("3", 6)
            Rectangle(3, "6")
            Rectangle(3, 6, "9")
            Rectangle(3, 6, 9, "12") 
            Rectangle(None)
            Rectangle(float("inf"))
            Rectangle(3.6, 9.1)
            raise TypeError()
        
        with self.assertRaises(ValueError):
            Rectangle(-8, 9)
            Rectangle(6, -9)
            Rectangle(0, 3)
            Rectangle(3, 0)
            Rectangle(3, 6, -9)
            Rectangle(3, 6, 9, -12)
            raise ValueError()

        self.assertEqual(t1.id, 3)
        self.assertEqual(t2.id, 12)

    def test_area(self):
        '''Testing area method'''
        t3 = Rectangle(3, 2)
        t4 = Rectangle(8, 7, 0, 0, 12)
        t5 = Rectangle(999, 999)

        self.assertEqual(t3.area(), 6)
        self.assertEqual(t4.area(), 56)
        self.assertEqual(t5.area(), 998001)
        

if __name__ == "__main__":
    unittest.main()
