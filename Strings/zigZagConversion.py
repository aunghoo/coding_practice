''' Medium

'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        cols = len(s)
        wordMatrix = [[''] * cols for i in range(numRows)]
        currentCol = 0
        currentRow = 0
        betweenChars = 0
        fillUp = False
        i = 0
        while i < len(s):
            if fillUp:
                currentRow -= 1
                currentCol += 1
                if currentRow > 0:
                    wordMatrix[currentRow][currentCol] = s[i]
                else:
                    currentRow = 0
                    fillUp = False
            if not fillUp:
                if currentRow < numRows:
                    wordMatrix[currentRow][currentCol] = s[i]
                    currentRow += 1
                elif currentRow == numRows:
                    currentRow -= 1
                    fillUp = True
                    i -= 1
            i += 1
        solution = ''
        for r in wordMatrix:
            for c in r:
                if c != '':
                    solution += c
        return solution
