import unittest
from homework2 import slicing
class MyTestCase(unittest.TestCase):
    def new_slicing (self):
        gen = slicing (5,6,6)
        self.assertEqual(slicing,0)


if __name__ == '__main__':
    unittest.main()
