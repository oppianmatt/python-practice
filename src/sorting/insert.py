'''
Created on Jul 4, 2012

@author: matt

Insertion sort example

'''

def sort(a):
    a = a[:]
    i = 0
    while (i < len(a) - 1):
        insert(a, i, a[i])
        i = i + 1
    return a

def insert(a, pos, val):
    i = pos - 1
    while (i >= 0 and a[i] > val):
        a[i+1] = a[i]
        i = i - 1
    a[i+1] = val


import unittest


class Test(unittest.TestCase):


    def testExamples(self):
        a = [2, 4, 1, 3, 5]
        sorteda = sorted(a)
        self.assertEqual(sort(a), sorteda)
        pass
    
    def testExtremes(self):
        a = []
        self.assertEqual(sorted(a), sort(a))
        a = [0]
        self.assertEqual(sorted(a), sort(a))
        a = [1]
        self.assertEqual(sorted(a), sort(a))
        a = [1, 2, 3, 4, 5]
        self.assertEqual(sorted(a), sort(a))
        a = [5, 4, 3, 2, 1]
        self.assertEqual(sorted(a), sort(a))
        a = range(0, 100)
        self.assertEqual(sorted(a), sort(a))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()