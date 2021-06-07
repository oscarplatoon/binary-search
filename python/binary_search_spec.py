# Write your unit tests here
import unittest
from unittest.main import main
from binary_search import binary_search

class BinarySearchTestCase(unittest.TestCase):

    def test_one(self):
        self.assertEqual(binary_search(1,[1,2,3,4,5]), 0)
    
    def test_two(self):
        self.assertEqual(binary_search(2,[1,2,3,4,5]), 1)

    def test_three(self):
        self.assertEqual(binary_search(3,[1,2,3,4,5]), 2)

    def test_four(self):
        self.assertEqual(binary_search(4,[1,2,3,4,5]), 3)

    def test_five(self):
        self.assertEqual(binary_search(5,[1,2,3,4,5]), 4)

    def test_six(self):
        self.assertEqual(binary_search(7,[1,5,7,2,3,8,4,9]), 5)
    
    def test_not_found(self):
        self.assertEqual(binary_search(6,[1,5,7,2,3,8,4,9]), -1)


if __name__ == '__main__':
    unittest.main
