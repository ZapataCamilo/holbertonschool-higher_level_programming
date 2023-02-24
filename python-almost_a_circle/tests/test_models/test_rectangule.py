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
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 6)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.width, 5)
        self.assertEqual(r3.height, 7)
        self.assertEqual(r3.x, 8)
        self.assertEqual(r3.y, 9)
