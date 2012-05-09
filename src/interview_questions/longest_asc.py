'''
Created on May 8, 2012

@author: matt

Given a an unordered list of numbers find the longest ascending (non adjacent) list of numbers

This is actually a tricky problem that has a linear solution. I'm not sure I'd expect someone to get a linear solution though without some help. 
[edit to add: the solution is n-log-n, not linear....]
http://www.reddit.com/r/programming/comments/f1bxw/my_facebook_interview_experience_xpost_from/c1ckwwn

'''

def longest_asc(A):
    pass

import unittest

class Test(unittest.TestCase):


    def testSimple(self):
        
        A = [1, 2, 3]
        self.assertEquals([1,2,3], longest_asc(A))
        
        A = [4, 2, 3]
        self.assertEquals([2,3], longest_asc(A))
        
        A = [4, 5, 1, 2, 3]
        self.assertEquals([1,2,3], longest_asc(A))
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()