# Write your unit tests here
import unittest
from binary_search import binary_search

test_array = [1,2,3,4,5]
super_big_array = [1,5,7,2,3,8,4,9]

class BinarySearchTest(unittest.TestCase):
    """Tests for binary_search.py"""

    def test_array_input(self):
        self.assertEqual(binary_search(test_array), test_array)

    def test_simple_array(self):
        self.assertEqual(binary_search(test_array), test_array)
        self.assertEqual(binary_search(1, test_array) == 0)
        self.assertEqual(binary_search(2, test_array) == 1)
        self.assertEqual(binary_search(3, test_array) == 2)
        self.assertEqual(binary_search(4, test_array) == 3)
        self.assertEqual(binary_search(5, test_array) == 4)

    def test_big_array(self):
        self.assertEqual(binary_search(7, super_big_array) == 5)
        self.assertEqual(binary_search(6, super_big_array) == -1)

# print(binary_search(1, test_array) == 0)
# print(binary_search(2, test_array) == 1)
# print(binary_search(3, test_array) == 2)
# print(binary_search(4, test_array) == 3)
# print(binary_search(5, test_array) == 4)

# print(binary_search(7, super_big_array) == 5)
# print(binary_search(6, super_big_array) == -1)

if __name__ == '__main__':
    unittest.main()