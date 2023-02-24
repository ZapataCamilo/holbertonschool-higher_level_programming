from models.base import Base
import unittest

class Base_Test(unittest.TestCase):
    def test_init(self):
        base1 = Base()
        self.assertEqual(base1.id, 1) 
        base_tow = Base(3)
        self.assertEquals(base_tow.id, 3)

    def test_to_json_string(self):
        json_string = Base(10)
        self.assertEqual(json_string.to_json_string(None), '[]')

        json_strng2 = Base(1)
        self.assertEqual(json_strng2.to_json_string({"Nombre": "Camilo", "Edad": 20}), '{"Nombre": "Camilo", "Edad": 20}')

        json_strng3 = Base()
        self.assertEqual(json_strng3.to_json_string([]), '[]')
        
    def test_to_from_json_string(self):
        str_json = [{'id': 89, 'width': 10, 'height': 4}]
        to_json = Base.to_json_string(str_json)
        self.assertEqual(Base.from_json_string(to_json), str_json)
  
if __name__ == '__main__':
    unittest.main()
