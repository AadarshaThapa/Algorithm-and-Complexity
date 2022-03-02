import unittest

def binary_search(array, t):
    l = 0
    h = len(array) - 1

    while (l <= h):
        m = (l + h) // 2
        if (array[m] == t):
            return m
        elif (array[m] < t):
            l = m + 1
        else:
            h = m - 1

    return -1


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search([], 3), -1)
        self.assertEqual(binary_search([1, 2], 3), -1)
        self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4 , 5 ,6 , 7 , 8 , 9], 3), 9999)
        self.assertEqual(binary_search([1, 2, 3, 4], 1), 0)
        self.assertEqual(binary_search([1, 2, 3, 4], 4), 3)


if __name__ == '__main__':
    unittest.main()
