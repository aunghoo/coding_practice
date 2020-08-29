#!/bin/python
# Twilio Hackerrank

import math
import os
import random
import re
import sys


#
# Complete the 'segments' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING message as parameter.
#

def segments(message):
    # variables needed
    segmentsList = []
    endSegment = 0
    startSegment = 0
    numSegs = 0
    # if the entire message can fit in a segment, then just put it.
    if len(message) <= 160:
        return [message]
    # condition for not starting a segment at end of message
    # start segment is the inclusive index, end segment is exclusive
    while (startSegment < len(message)):
        endSegment += 155
        endSegment = min(endSegment, len(message))
        # if end segment aligns nicely at the end of a word, then segment is ready
        if endSegment == len(message) or message[endSegment] == ' ':
            segmentsList.append(message[startSegment:endSegment])
            startSegment += 155
        # otherwise needs some string magic
        else:
            # find where we can properly end the segment, which is at the
            # space character. So retract until we find the space character
            i = endSegment - 1
            while(message[i] != ' '):
                i -= 1
            endSegment = i + 1
            segmentsList.append(message[startSegment:endSegment])
            startSegment = i + 1
        # keep track of number of segments for the suffix
        numSegs += 1

    # add the suffixes
    for i in range(len(segmentsList)):
        suf = '(' + str(i+1) + '/' + str(numSegs) + ')'
        segmentsList[i] += suf

    return segmentsList
