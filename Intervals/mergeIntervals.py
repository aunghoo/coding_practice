''' Medium
https://leetcode.com/problems/merge-intervals
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mergedIntervals = []
        seen = set()
        for start, end in intervals:
            self.helperMerge(start, end, intervals, mergedIntervals, seen)
        return mergedIntervals

    def helperMerge(self, start, end, intervals, mergedIntervals, seen):
        for i, inv in enumerate(intervals):
            if i in seen:
                continue
            ms, me = inv[0], inv[1]
            if start >= ms and start <= me:
                start = min(start, ms)
                end = max(end, me)
                seen.add(i)

        toDelete = []
        for i, inv in enumerate(mergedIntervals):
            ms, me = inv[0], inv[1]
            if start >= ms and start <= me:
                start = min(start, ms)
                end = max(end, me)
                toDelete.append([ms,me])

        for d in toDelete:
            mergedIntervals.remove(d)
        mergedIntervals.append([start, end])
