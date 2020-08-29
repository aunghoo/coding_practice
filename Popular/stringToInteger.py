''' Medium
https://leetcode.com/problems/string-to-integer-atoi/
'''

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        neg = False
        integer = 0
        stringInteger = ''
        while i < len(str) and str[i] == ' ':
            i += 1
        if i >= len(str):
            return 0
        if str[i] == '-':
            neg = True
            i += 1
        elif str[i] == '+':
            i += 1
        while i < len(str) and '0' <= str[i] <= '9':
            stringInteger += str[i]
            i += 1
        if len(stringInteger) == 0:
            return 0
        mult = 1
        reversedStringInteger = stringInteger[::-1]
        for c in reversedStringInteger:
            integer += int(c) * mult
            mult *= 10
        if neg:
            integer = -integer
        if integer > (2**31 - 1):
            integer = 2**31 - 1
        if integer < (-2**31):
            integer = (-2**31)
        return integer
