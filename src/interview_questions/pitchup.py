'''

Write a program to find a pitch based on this clue: "Join us at pitch x. x is a
number between 1 and 553 such that the sum of x's divisors (not including x) is
greater than x but no subset of x's divisors add up to exactly x."

Created on May 29, 2012

@author: oppianmatt
'''

import math

MAX_X = 553
DEBUG = True

def find_pitch():
    pitches = []
    for x in xrange(1, MAX_X+1):
        divs = get_divisors(x)
        sum_divs = sum(divs)
        if sum_divs > x:
            # check if subset of divs don't add to x
            if not check_subset_sum(divs, x):
                pitches.append(x)
                if DEBUG:
                    print "x=%s divisors(%s)" % (x, divs)
    return pitches
        
DIVS = {}
def get_divisors(x):
    # check memoziation
    if DIVS.has_key(x):
        return DIVS[x]
    
    # hold divisors, start with 1 as always divisor
    divisors = set([1])
    # go from 2 to sqrt(x) to find divisors
    # so we skip 1 and x as divisors
    for i in xrange(2, int(math.sqrt(x))+1):
        # does i divide without remainder?
        (q, mod) = divmod(x, i)
        if mod == 0:
            # add the number and the quotient
            # set ensures no duplicates
            divisors.add(i)
            divisors.add(q)

    # save in memoziation
    DIVS[x] = divisors
    return divisors

def check_subset_sum(iterable, x):
    # create combinations of iterable to see if they add to x
    # combinations with less than 3 can never add to x
    # could probably optimize this further
    for i in xrange(len(iterable), 2, -1):
        comb = combinations(iterable, i)
        for c in comb:
            if sum(c) == x:
                return True
    return False
    
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    # taken from itertools python3
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def main():
    find_pitch()

import unittest

class Test(unittest.TestCase):

    def testName(self):
        pitches = find_pitch()
        self.assertEqual(70, pitches[0])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()