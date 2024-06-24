import unittest
from models.amenity import Amenity
from datetime import datetime

class TestAmenity(unittest.Testcase):
    """testcase for class Amenity"""
    def test_initialization(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertIsIstance(amenity.created_at, datetime)
        self.assertIsIstance(amenity.updated_at, datetime)
        self.assertEqual(amenity.name, "")

    def test_save(self):
        """test method for save"""
        amenity = Amenity()
        initial_updated_at = amenity.updated_at
        amenity.save()
        self.assertNot(ammenity.updated_at, initial_updated_at)

     def test_todict(self):
        """Test method for dict"""
        a1 = Amenity()
        a2 = Amenity(**a1.to_dict())
        a_dict = a2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(a2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(a1, a2)

     def test_str(self):
        """Test method for str representation"""
        a1 = Amenity()
        string = f"[{type(a1).__name__}] ({a1.id}) {a1.__dict__}"
        self.assertEqual(a1.__str__(), string)

if __name__ == "__main__":
    unittest.main()
