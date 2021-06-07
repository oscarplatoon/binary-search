import unittest

from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    """
    Test binary search returns an integer:
    """
    def test_returns_a_value(self):
        self.assertEqual(type(binary_search(3, [1,2,3,4], 0, 4)), type(4))

    """
    Test Binary Search:
    """
    def test_accuracy_of_search(self):
        test_array = [1,2,3,4,5]

        self.assertTrue(binary_search(1, test_array, 0, len(test_array)) == 0)

        self.assertTrue(binary_search(2, test_array, 0, len(test_array) == 1))

        self.assertTrue(binary_search(3, test_array, 0, len(test_array) == 2))

        self.assertTrue(binary_search(4, test_array, 0, len(test_array)) == 3)

        self.assertTrue(binary_search(5, test_array, 0, len(test_array)) == 4)

    """
    Test Larger Arrays to confirm functionality:
    """

    def test_large_array_accuracy(self):
        super_big_array = [1,5,7,2,3,8,4,9]

        self.assertTrue(binary_search(7, super_big_array, 0, len(super_big_array)) == 5)

        self.assertTrue(binary_search(6, super_big_array, 0, len(super_big_array)) == -1)

if __name__ == '__main__':
    unittest.main()
