import unittest
from binary_search import binary_search

class BinaryTest(unittest.TestCase):
    test_array = [1,2,3,4,5]
    super_big_array = [1,5,7,2,3,8,4,9]

    def test_1(self):
        self.assertEqual(binary_search(1, self.test_array),0)

    def test_2(self):
        self.assertEqual(binary_search(2, self.test_array),1)

    def test_3(self):
        self.assertEqual(binary_search(3, self.test_array),2)

    def test_4(self):
        self.assertEqual(binary_search(4, self.test_array),3)

    def test_5(self):
        self.assertEqual(binary_search(5, self.test_array),4)

    def test_6(self):
        self.assertEqual(binary_search(7, self.super_big_array),5)

    def test_7(self):
        self.assertEqual(binary_search(6, self.super_big_array),-1)


if __name__ == '__main__':
    unittest.main()
