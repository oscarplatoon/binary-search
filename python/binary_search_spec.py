# Write your unit tests here
import unittest
from binary_search import binary_search
from binary_search import middle_index

class BinarySearchUnitTest(unittest.TestCase):

    def test_middle_index_odd(self):
        self.assertEqual(middle_index([1,2,3,4,5]), 3)
    
    def test_middle_index_even(self):
        self.assertEqual(middle_index([1,2,3,4]), 2)

    def test_odd_search(self):
        self.assertEqual(binary_search(2, [1,2,3,4,5]), 1)

    def test_even_search(self):
        self.assertEqual(binary_search(6, [1,2,3,4,5,6]), 5)
        
if __name__ == '__main__':
    unittest.main()

# test_array = [1,2,3,4,5]

# print(binary_search(1, test_array) == 0)
# print(binary_search(2, test_array) == 1)
# print(binary_search(3, test_array) == 2)
# print(binary_search(4, test_array) == 3)
# print(binary_search(5, test_array) == 4)


# super_big_array = [1,5,7,2,3,8,4,9]
# print(binary_search(7, super_big_array) == 5)
# print(binary_search(6, super_big_array) == -1)
