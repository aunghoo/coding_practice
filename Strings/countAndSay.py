''' Easy
https://leetcode.com/problems/count-and-say/
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        sequence = '1'
        for c in range(n-1):
            sequence = getNextSequence(sequence)
        return sequence

def getNextSequence(s):
    nextSequence = ''
    prev = s[0]
    count = 0
    for i in s:
        if i == prev:
            count += 1
        else:
            nextSequence += (str(count) + prev)
            count = 1
        prev = i
    nextSequence += (str(count)) + prev
    return nextSequence
