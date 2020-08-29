''' Medium
https://leetcode.com/problems/reverse-integer/
'''

# got 2 solutions
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rem = 1
        divider = 1
        reversedInt = 0
        neg = True if x < 0 else False
        if neg:
            x = x * (-1)
        while True:
            rem = x/divider
            if (rem == 0):
                break
            divider = divider * 10
        divider = divider/10
        mult = 1
        while divider != 0:
            reversedInt += (x / divider) * mult
            x = x % divider
            mult = mult * 10
            divider = divider/10
        if neg:
            reversedInt *= -1
        return reversedInt if -2**31<reversedInt<2**31-1 else 0

    def stringReverseMethod(self, x):
        x = list(str(x))
        if x[0] == '-':
            x[:] = [x[0]] + x[-1:0:-1]
        else:
            x[:] = x[-1::-1]
        string_number = ''
        for i in range(len(x)):
            string_number += x[i]
        return int(string_number) if -2**31<int(string_number)<2**31-1 else 0
