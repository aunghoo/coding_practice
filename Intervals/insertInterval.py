''' Hard
https://leetcode.com/problems/insert-interval
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval
        startMerge, endMerge = False, False
        startPosition, endPosition = len(intervals), len(intervals)
        # start with finding insert position
        for i, interval in enumerate(intervals):
            end = interval[1]
            if newStart <= end:
                startPosition = i
                if intervals[startPosition][0] <= newStart and intervals[startPosition][1] >= newStart:
                    startMerge = True
                elif intervals[startPosition][0] > newStart:
                    startPosition = i-1  
                break
        # find ending position
        for i in range(len(intervals)):
            end = intervals[i][1]
            if newEnd <= end:
                endPosition = i
                if intervals[endPosition][0] <= newEnd and intervals[endPosition][1] >= newEnd:
                    endMerge = True
                break

        newIntervals = []

        # insert intervals before new interval
        if startMerge:
            newIntervals.extend(intervals[:startPosition])
            newStart = min(intervals[startPosition][0], newStart)
        else:
            newIntervals.extend(intervals[:startPosition+1])

        # insert the new interval and the rest based on end merge on not
        if endMerge:
            newEnd = max(intervals[endPosition][1], newEnd)
            newIntervals.append([newStart, newEnd])
            newIntervals.extend(intervals[endPosition+1:])
        else:
            newIntervals.append([newStart, newEnd])
            newIntervals.extend(intervals[endPosition:])

        intervals = newIntervals
        return newIntervals