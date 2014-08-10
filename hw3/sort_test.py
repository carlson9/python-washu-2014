from sort import *
import unittest

class PortfolioTest(unittest.TestCase):
    def setUp(self):
        self.test1 = [1,6,4,8,4,6,8,45,2,54,23,54]
        self.sort1 = [1,2,4,4,6,6,8,8,23,45,54,54]
        self.test2 = ['a','d','q','l','p']
        self.sort2 = ['a','d','l','p','q']
        self.test3 = [1,65,34,'a','g',23,'b']
        self.sort3 = [1,23,34,65,'a','b','g']

    def test_merge_sort(self):
        self.assertEqual(self.sort1, merge_sort(self.test1))
        self.assertEqual(self.sort2, merge_sort(self.test2))
        self.assertEqual(self.sort3, merge_sort(self.test3))

    def test_item_sort(self):
        self.assertEqual(self.sort1, item_sort(self.test1))
        self.assertEqual(self.sort2, item_sort(self.test2))
        self.assertEqual(self.sort3, item_sort(self.test3))
                
if __name__ == '__main__':
    unittest.main()
