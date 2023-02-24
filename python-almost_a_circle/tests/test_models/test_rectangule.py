from models.rectangle import Rectangle
import unittest

class Rectangle_Test(unittest.TestCase):
    def test_init(self):
        rec = Rectangle(1, 2)
        self.assertEqual(rec.id, 1)

        rec2 = Rectangle(1, 4, 7, 5, 10)
        self.assertEqual(rec2.id, 10)
