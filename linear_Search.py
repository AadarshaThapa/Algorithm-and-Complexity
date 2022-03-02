import unittest
from search import linearsearch
from binary_search import binary_search

class SearchTestCase(unittest.TestCase):

    def test_linear_search(self):

        values =[1,5,8,4,6,7,0]
        self.assertEqual(linearsearch(values,5),1)
        self.assertEqual(linearsearch(values,4),3)
        self.assertEqual(linearsearch(values,9),-1)

    def test_binarysearch(self):
        values= [0,1,2,3,4,5,6,7,8,9]   
        self.assertEqual(binary_search(values,1),1)
        self.assertEqual(binary_search(values,4),5)
        self.assertEqual(binary_search(values,9999),-1) 
        self.assertEqual(binary_search(values,100000),-1) 


    if __name__ == '__main__':
        unittest.main()

