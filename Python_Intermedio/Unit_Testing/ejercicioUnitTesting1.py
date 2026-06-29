import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Python_Intermedio.Sorting_Algorithms.ejercicioOrdenamiento1 import bubble_sort
import unittest

class TestBubbleSort(unittest.TestCase):
    def test_works_with_small_list(self):
        result = bubble_sort([5, 3, 8, 1])
        expected = [1,3,5,8]
        self.assertEqual(result, expected)

    def test_works_with_large_list(self):
        large_list = list(range(150, 0, -1))
        expected_result = list(range(1,151))

        result = bubble_sort(large_list)
        self.assertEqual(result, expected_result)

    def test_works_with_empty_list(self):
        result = bubble_sort([])
        self.assertEqual(result, [])

    def test_does_not_work_with_empty_parameter(self):
        with self.assertRaises(TypeError):
            bubble_sort("not a list")

if __name__ == '__main__':
    unittest.main()