'''
Created on May 8, 2012

@author: matt

Example merge sort
'''
from random import Random

    
def merge_sort(left, right=None):
    
    if right == None:
        mid = len(left) / 2
        return merge_sort(left[:mid], left[mid:])
    
    # handle no length
    if not left: return right
    if not right: return left
    
    # handle lengths of 1
    if len(left) == len(right) == 1:
        if left[0] > right[0]:
            # swap
            return [right[0], left[0]]
        # left and right sorted in order and length of 1 each so return as new array
        return [left[0], right[0]]
        
    # split left and right and sort those
    mid = (len(left) / 2) or 1
    left = merge_sort(left[:mid], left[mid:])
        
    # split right and sort those
    mid = (len(right) / 2) or 1
    right = merge_sort(right[:mid], right[mid:])
    
    # merge
    A = []
    for i in xrange(len(left) + len(right)):
        l = None
        r = None
        
        if len(left):
            l = left[0]
        else:
            # no more left so append all of right
            A.extend(right)
            return A
        
        if len(right):
            r = right[0]
        else:
            # no more right
            A.extend(left)
            return A
            
        # if left is smaller then put it next, otherwise r
        if l <= r:
            A.append(l)
            del left[0]
        else:
            A.append(r)
            del right[0]
    return A
        

import unittest


class Test(unittest.TestCase):


    def testSimple(self):
        self.assertEqual([1, 2, 3], merge_sort([3, 2, 1]))
        self.assertEqual([1, 2, 3], merge_sort([1, 3, 2]))
        
        self.assertEqual([1, 3, 4, 4, 5, 5, 7, 8], merge_sort([4, 5, 1, 7, 8, 4, 3, 5]))
        
    def testRandom10(self):
        random = Random()
        pop = range(10) + range(10)
        A = random.sample(pop, 10)
        self.assertEquals(sorted(A), merge_sort(A))
        
    def testRandom32767(self):
        random = Random()
        max = 32767
        pop = range(max) + range(max)
        A = random.sample(pop, max)
        self.assertEquals(sorted(A), merge_sort(A))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSimple']
    unittest.main()