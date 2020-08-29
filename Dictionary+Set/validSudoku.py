''' Medium
https://leetcode.com/problems/valid-sudoku
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check rows
        for r in range(len(board)):
            record = set()
            for c in range(len(board[r])):
                if board[r][c] in record:
                    return False
                if board[r][c] != '.':
                    record.add(board[r][c])

        # check columns
        for c in range(len(board[0])):
            record = set()
            for r in range(len(board)):
                if board[r][c] in record:
                    return False
                if board[r][c] != '.':
                    record.add(board[r][c])

        # check grids
        for i in range(0, 3):
            c = i * 3
            for j in range(0, 3):
                r = j * 3
                record = set()
                for k in range(0, 3):
                    for l in range(0, 3):
                        if board[r+k][c+l] in record:
                            return False
                        if board[r+k][c+l] != '.':
                            record.add(board[r+k][c+l])

        return True
