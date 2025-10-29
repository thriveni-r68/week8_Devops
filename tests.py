import unittest
from main import to_upper

class TestStringMethods(unittest.TestCase):
    def test_uppercase(self):
        self.assertEqual(to_upper("cloud"), "CLOUD")

if __name__ == "__main__":
    unittest.main()
