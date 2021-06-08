# Write your unit tests here
import unittest
from binary_search import binary_search

test_array  = [1,2,3,4,5]
big_array   = [1,5,7,2,3,8,4,9]
super_array = [12,43,55,65,68,90,35,69,22,25,29,31,50,100,101,110]


class BinarySearchTest(unittest.TestCase):
    """Tests for binary_search.py"""

    def test_simple_array(self):
        self.assertEqual(binary_search(1, test_array), 0)
        self.assertEqual(binary_search(2, test_array), 1)
        self.assertEqual(binary_search(3, test_array), 2)
        self.assertEqual(binary_search(4, test_array), 3)
        self.assertEqual(binary_search(5, test_array), 4)

    def test_big_array(self):
        self.assertEqual(binary_search(7, big_array), 5)
        self.assertEqual(binary_search(6, big_array), -1)

    def test_super_array(self):
        self.assertEqual(binary_search(12, super_array), 0)
        self.assertEqual(binary_search(69, super_array), 11)
        self.assertEqual(binary_search(90, super_array), 12)
        self.assertEqual(binary_search(100, super_array), 13)
        self.assertEqual(binary_search(50, super_array), 7)
        self.assertEqual(binary_search(88, super_array), -1)

    def test_duplicate_num(self):
        pass

if __name__ == '__main__':
    unittest.main()