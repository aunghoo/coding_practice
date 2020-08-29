''' Easy
https://leetcode.com/problems/roman-to-integer/
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        assumes that all input are valid roman numerals
        """
        integer = 0
        i = 0
        while i < len(s):
            special = 0
            curNum = convertToInt(s[i])
            if i + 1 < len(s):
                nextNum = convertToInt(s[i+1])
                if nextNum > curNum:
                    curNum = nextNum - curNum
                    i += 1
            integer += curNum
            i += 1
        return integer

def convertToInt(s):
    if s == 'I':
        return 1
    elif s == 'V':
        return 5
    elif s == 'X':
        return 10
    elif s == 'L':
        return 50
    elif s == 'C':
        return 100
    elif s == 'D':
        return 500
    elif s == 'M':
        return 1000
    else:
        return -1
