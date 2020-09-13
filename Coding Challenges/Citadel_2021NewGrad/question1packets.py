#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'droppedRequests' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY requestTime as parameter.
#

def droppedRequests(requestTime):
    # Write your code here

    totalDropped = 0
    # requests since time t
    requestsSince = {}
    currentSecond = requestTime[0]
    currentSecondRequests = 0
    for index, t in enumerate(requestTime):
        satisfied = True
        if t not in requestsSince:
            requestsSince[t] = 0
        if currentSecond == t and currentSecondRequests >= 3:
            satisfied = False
        if satisfied:
            # find the first second in last 10 sec window
            for i in range(t-9, t):
                if i in requestsSince and requestsSince[i] >= 20:
                    satisfied = False
                    break
        if satisfied:
            # find the first second in last 1 min window
            for i in range(t-59, t):
                if i in requestsSince and requestsSince[i] >= 60:
                    satisfied = False
                    break
        # update requests made since for each starting times
        if t not in requestsSince:
            requestsSince[t] = 0
        for k in requestsSince:
            requestsSince[k] += 1
        # update how many requests so far for current second
        if currentSecond != t:
            currentSecond = t
            currentSecondRequests = 0
        currentSecondRequests += 1

        if not satisfied:
            totalDropped += 1

    return totalDropped
        