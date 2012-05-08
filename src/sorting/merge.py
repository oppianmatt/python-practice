'''
Created on May 8, 2012

@author: matt

Example merge sort
'''
from random import Random

    
def merge_sort(A):
    
    # handle len of 1
    if len(A) == 1: return A
    
    # handle lengths of 2
    if len(A) == 2:
        if A[0] > A[1]:
            # swap
            return [A[1], A[0]]
        # already sorted
        return A
        
    # split left those
    mid = (len(A) / 2) or 1
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
        
    # merge
    return merge(left, right)

def merge(left, right):
    A = []
    while len(left) or len(right):

        if len(left) and len(right):
            if left[0] <= right[0]:
                A.append(left[0])
                del left[0]
            else:
                A.append(right[0])
                del right[0]
        # look for end of left or right
        if not len(left):
            A.extend(right)
            break
        elif not len(right):
            A.extend(left)
            break
        
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