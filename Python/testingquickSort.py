# test_quicksort.py

import unittest
from quickSort import quick_sort  # Import the quicksort function from quicksort.py

class TestQuickSort(unittest.TestCase):
    
    def test_sorted_array(self):
        self.assertEqual(quick_sort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])

    def test_empty_array(self):
        self.assertEqual(quick_sort([]), [])

    def test_single_element(self):
        self.assertEqual(quick_sort([5]), [5])

    def test_duplicates(self):
        self.assertEqual(quick_sort([4, 5, 4, 3, 2, 1, 1]), [1, 1, 2, 3, 4, 4, 5])

if __name__ == '__main__':
    unittest.main()
