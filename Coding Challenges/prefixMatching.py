#!/bin/python
# Twilio Hackerrank

import math
import os
import random
import re
import sys


#
# Complete the 'match' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY prefixes
#  2. STRING_ARRAY numbers
#

def match(prefixes, numbers):
    # store all the prefixes in a hashmap
    preMap = {}
    maxLength = 0
    for s in prefixes:
        if len(s) > maxLength:
            maxLength = len(s)
        preMap[tuple(s)] = s

    # for each number, check if prefixes exist in the hashmap
    maxPrefixes = []
    for n in numbers:
        exists = False
        maxSoFar = ''
        # vary the length of prefix
        # this iteration is O(k) when k is lenght of string n
        for l in reversed(range(min(maxLength+1, len(n)))):
            prefixInterested = n[:l]
            # if we found the prefix break
            # thankfully, O(1) lookup due to hashmap
            if tuple(prefixInterested) in preMap:
                maxSoFar = preMap[tuple(prefixInterested)]
                exists = True
                break
        # if prefix exists then add the prefix
        if exists:
            maxPrefixes.append(maxSoFar)
        # if prefix does not exist then just add an empty string
        else:
            maxPrefixes.append('')
    return maxPrefixes

    

# There is a bug on line 36 - should be len(n)+1
