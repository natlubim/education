import unittest
import maximum

class MaxTests(unittest.TestCase):
    def test_max(self):
        mas = [0,99]
        self.assertEqual(99, maximum.findmax(mas))



if __name__ == '__main__':
    unittest.main()
