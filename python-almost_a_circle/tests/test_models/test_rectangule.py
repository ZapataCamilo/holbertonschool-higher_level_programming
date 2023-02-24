import unittest
from models.rectangle import Rectangle

class Rectangle_Test(unittest.TestCase):
    
    def test_init(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(3, 5, 6)
        r3 = Rectangle(5, 7, 8, 9, 10)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 10)
