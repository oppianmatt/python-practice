'''
Created on May 8, 2012

@author: matt

You are given an array full of positive integers. Write a function that returns
the largest sum you can get by adding together numbers in non-adjacent indices
from the array. I.e. you if you include the things stored in arr[i] in your sum,
you can't include what is stored in arr[i-1] or arr[i+1]

'''

def largest_sum_non_adj(A):
    pass

import unittest


class Test(unittest.TestCase):


    def testSimple(self):
        A = [1, 2, 3]
        self.assertEquals(4, largest_sum_non_adj(A))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
