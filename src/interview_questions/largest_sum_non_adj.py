'''

Question
========

You are given an array full of positive integers. Write a function that returns
the largest sum you can get by adding together numbers in non-adjacent indices
from the array. I.e. you if you include the things stored in arr[i] in your sum,
you can't include what is stored in arr[i-1] or arr[i+1]

Examples
========

A = [1, 2, 3]

Should return 4 which can be found from:

[1, 0, 3]

Another more complex example:

Given A = [1, 2, 100, 4, 5, 100, 7, 8, 100, 10]

It should return 301 which is comprised of:

[1, 0, 100, 0, 0, 100, 0, 0, 100,  0]

Solution
========

Current solution is to calculate the number of permutations using gaps of 2 or 3
(any more will be included in those series) Gaps of 4 can have one in the middle
so we discount those and gaps of 5 can be a gap of 2 and 3 so discount those.
Gaps of 6 are 2 gaps of 3 etc.

So example:

[1, 2, 100, 4, 5, 100, 7, 8, 100, 10]

We have the following permutations:

[1, 0, 100, 0, 5,   0, 7, 0, 100,  0] sum = 213
[1, 0, 100, 0, 5,   0, 7, 0,   0, 10] sum = 123
[1, 0, 100, 0, 5,   0, 0, 8,   0, 10] sum = 124
[1, 0, 100, 0, 0, 100, 0, 8,   0, 10] sum = 219
[1, 0, 100, 0, 0, 100, 0, 0, 100,  0] sum = 301
[1, 0,   0, 4, 0, 100, 0, 8,   0, 10] sum = 123
[1, 0,   0, 4, 0, 100, 0, 0, 100,  0] sum = 205
[1, 0,   0, 4, 0,   0, 7, 0, 100,  0] sum = 112
[1, 0,   0, 4, 0,   0, 7, 0,   0, 10] sum =  22
[0, 2,   0, 4, 0, 100, 0, 8,   0, 10] sum = 124
[0, 2,   0, 4, 0, 100, 0, 0, 100,  0] sum = 206
[0, 2,   0, 4, 0,   0, 7, 0, 100,  0] sum = 113
[0, 2,   0, 4, 0,   0, 7, 0,   0, 10] sum =  23
[0, 2,   0, 0, 5,   0, 7, 0, 100,  0] sum = 114
[0, 2,   0, 0, 5,   0, 7, 0,   0, 10] sum =  24
[0, 2,   0, 0, 5,   0, 0, 8,   0, 10] sum =  25

The largest being 301

'''
def largest_sum_non_adj(A):
    '''
    This algorithm works out the number of permutations the list can have using
    gaps of 2 or 3. Uses more memory than naive but is a lot faster.
    '''
    maximum_number_of_items = len(A)
    
    maximum = 0
    if maximum_number_of_items == 0:
        return maximum
    
    stack = [[0], [A[0]]]
    
    while len(stack) > 0:
        current = stack.pop()
        while len(current) < maximum_number_of_items:
            
            current_length = len(current)
            
            # default is to add a zero
            next_item = 0
            
            if current[-1] == 0:
                # we had a zero at the end of the currently considered items
                next_item = A[current_length]
                if current_length > 1 and current[-2] != 0 and current_length < maximum_number_of_items - 1:
                    # we put the zero option on the stack to evaluate later
                    other_option = current[:]
                    other_option.append(0)
                    stack.append(other_option)
                        
            current.append(next_item)
        
        maximum = max(maximum, sum(current))
        
    return maximum



def largest_sum_non_adj_naive(A):
    """
    we want to try every 2nd or 3rd (and every combinbation of those) since
    trying every 4th means we could do the 2nds in between and every gap of N
    can be filled with either a 2 or 3 gap eg a gap of 5 is a 2 and a 3
    
    While naive and slow, it uses less memory (n/2) array of gaps
    """
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
    values are 2 and 3. When you increment from 3 it goes to 2 with a carry to
    the next. If the carry overflows to the end, we have reached the end so zero
    out the list.
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
        

from random import randrange
import time
import unittest

class Test(unittest.TestCase):


    def do_random_test(self, length):
        A = [randrange(1, 1000000) for n in xrange(length)]; n = n

        start_time = time.time()
        answer = largest_sum_non_adj(A)
        calc_time = time.time() - start_time
        
        
        start_time = time.time()
        naive_answer = largest_sum_non_adj_naive(A)
        naive_answer = answer
        naive_time = time.time() - start_time
        
        print "random test of length (%d) - naive time = %.3f, calc time = %.3f" % (length, naive_time, calc_time)
        self.assertEquals(naive_answer, answer)
        
        
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
    
    def testRandom(self):  
        self.do_random_test(10)
        self.do_random_test(20)
        self.do_random_test(30)
        self.do_random_test(40)
        
 
    def testPerms(self):
        size = 30
        range = [x for x in xrange(1, size + 1)]
        for i in xrange(size):
            largest_sum_non_adj(range[:i])
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
