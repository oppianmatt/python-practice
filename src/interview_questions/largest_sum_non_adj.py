'''
Created on May 8, 2012

@author: matt

You are given an array full of positive integers. Write a function that returns
the largest sum you can get by adding together numbers in non-adjacent indices
from the array. I.e. you if you include the things stored in arr[i] in your sum,
you can't include what is stored in arr[i-1] or arr[i+1]

TODO:
ways to optimize could be to remember ones we have added before for gaps and indexes that we have added before

'''

def largest_sum_non_adj(A):
    '''
    we want to try every 2nd or 3rd (and every combinbation of those)
    since trying every 4th means we could do the 2nds in between
    and every gap of N can be filled with either a 2 or 3 gap
    eg a gap of 5 is a 2 and a 3
    '''
    maximum = 0
    # create an array to keep track of gaps
    gap_array = [2] * (len(A) / 2)
                       
    # loop through until gap_array can't be "incremented"
    while gap_array:
        # find the sum using gap_array, try both offset 0 and 1
        maximum = max(maximum, find_sum(A, gap_array), find_sum(A, gap_array, 1))
        # increment gap_array
        inc_gaps(gap_array)
        
    return maximum 

def inc_gaps(gaps, overflow=3):
    '''
    Gaps is a list with only 2 possible values (so like a list of bits) but the
    values are 2 and 3. When you increment from 3 it goes to 2 with a carry to the next.
    If the carry overflows to the end, we have reached the end so zero out the list.
    '''
    index = 0
    gaps[index] += 1
    
    # we have overflowed
    while index < len(gaps) and gaps[index] > overflow:
        # go back to 2
        gaps[index] = 2
        # move onto next gap
        index += 1
        # add the carry
        if index < len(gaps): gaps[index] += 1
        
    # check if we reached the end
    if index >= len(gaps):
        # reached the end so zero out and leave
        gaps[:] = []
    

def find_sum(A, gaps, offset=0):
    '''
    Loop through A but use the gaps list as a list to specify which index to
    goto next
    '''
    index = offset
    # start with first element
    sum = A[index]
    for gap in gaps:
        # increment the index by the next gap amount
        index += gap
        # see if we are off the end
        if index >= len(A): 
            # we have gone off the end
            break
        # now sum the element at that index
        sum += A[index]
    return sum
        

import unittest


class Test(unittest.TestCase):


    def testSimple(self):
        A = [1, 2, 3]
        self.assertEquals(4, largest_sum_non_adj(A))
        A = [1, 20, 3]
        self.assertEquals(20, largest_sum_non_adj(A))
        A = [1, 2, 3, 4, 5, 6]
        self.assertEquals(12, largest_sum_non_adj(A))
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEquals(30, largest_sum_non_adj(A))
        A = [1, 2, 3, 4, 5, 6, 7, 8, 20, 10]
        self.assertEquals(36, largest_sum_non_adj(A))
        A = [1, 2, 3, 4, 5, 15, 7, 8, 11, 10]
        self.assertEquals(39, largest_sum_non_adj(A))
        A = [1, 2, 3, 4, 5, 15, 7, 8, 20, 10]
        self.assertEquals(41, largest_sum_non_adj(A))
        A = [1, 2, 100, 4, 5, 100, 7, 8, 100, 10]
        self.assertEquals(301, largest_sum_non_adj(A))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
