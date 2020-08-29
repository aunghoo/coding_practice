''' Medium
https://leetcode.com/problems/rotate-image
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for loop in range((len(matrix)+1)/2):
            for pos in range(loop, len(matrix)-1-loop):
                last = len(matrix)-1
                top = matrix[loop][pos]
                #top takes left
                matrix[loop][pos] = matrix[last-pos][loop]
                #left takes bottom
                matrix[last-pos][loop] = matrix[last-loop][last-pos]
                #bottom takes right
                matrix[last-loop][last-pos] = matrix[pos][last-loop]
                #right takes top
                matrix[pos][last-loop] = top
        return matrix

# Also, rotating = flipping diagonally/ transposing + flipping horizontally
def rotateByFlipping(matrix):
    
