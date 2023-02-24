from models.rectangle import Rectangle
from models.base import Base
import unittest

class Rectangle_Test(unittest.TestCase):
    def test_init(self):
        rec = Rectangle(1, 2)
        self.assertEqual(rec.id, 1)

        rec2 = Rectangle(1, 4, 7)
        self.assertEqual(rec2.id, 2)

        rec3 = Rectangle(1, 3, 6, 7)
        self.assertEqual(rec3.id, 3)
