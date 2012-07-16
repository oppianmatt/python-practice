'''
Created on May 9, 2012

@author: matt

# Facebook logo stickers cost $2 each from the company store. I have an idea.
# I want to cut up the stickers, and use the letters to make other words/phrases.
# A Facebook logo sticker contains only the word 'facebook', in all lower-case letters.
#
# Write a function that, given a string consisting of a word or words made up
# of letters from the word 'facebook', outputs an integer with the number of
# stickers I will need to buy.
# foo('coffee kebab') -> 3
#
# You can assume the input you are passed is valid, that is, does not contain
# any non-'facebook' letters, and the only potential non-letter characters
# in the string are spaces.



'''
import math

WORD = "facebook "

def foo(s):
        
    count = {}
    for c in WORD:
        count[c] = (count[c]+1) if (c in count) else 1
    
    input_count = {}    
    for c in s:
        input_count[c] = (input_count[c]+1) if (c in input_count) else 1
    
    max_stickers = 0
    for letter in input_count:
        num_needed = input_count[letter]
        num_in_one_sticker = count[letter]
        num_stickers_needed = int(math.ceil(float(num_needed) / float(num_in_one_sticker)))
        max_stickers = max(num_stickers_needed, max_stickers)
    
    return max_stickers
    
    
import unittest


class Test(unittest.TestCase):


    def testExample(self):
        self.assertEquals(3, foo("coffee kebab"))
        self.assertEquals(1, foo("facebook"))
        self.assertEquals(2, foo("facebook facebook"))
        self.assertEquals(1, foo("face book"))
        self.assertEquals(3, foo("facefacebookface"))
        self.assertEquals(2, foo("faceboook"))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()