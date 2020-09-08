''' Medium
https://leetcode.com/problems/word-search
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def checkExists(board, r, c, seen, word, index):
            if (r,c) in seen:
                index -= 1
                return False

            seen.add((r,c))
            if board[r][c] == word[index] and index == len(word)-1:
                return True
            if board[r][c] != word[index]:
                index -= 1
                seen.remove((r,c))
                return False
            neighbors = ((r-1, c), (r+1, c), (r, c-1), (r,c+1))
            for nr, nc in neighbors:
                if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]):
                    if checkExists(board, nr, nc, seen, word, index+1):
                        return True
            index -= 1
            seen.remove((r,c))
            return False


        for r in range(len(board)):
            for c in range(len(board[0])):
                seen = set()
                if checkExists(board, r, c, seen, word, 0):
                    return True
        return False