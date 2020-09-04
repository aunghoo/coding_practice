''' Medium
https://leetcode.com/problems/pacific-atlantic-water-flow
'''

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        R = len(matrix)
        C = len(matrix[0])
        pacificData = [[0] * C for i in range(R)]
        atlanticData = [[0] * C for i in range(R)]

        # Top row and first column is for Pacific
        for r, c in [(0, col) for col in range(C)] + [(row, 0) for row in range(R)]:
            self.visit(r, c, matrix, pacificData)

        # Last column and bottom row is for Atlantic
        for r, c in [(row, C-1) for row in range(R)] + [(R-1, col) for col in range(C)]:
            self.visit(r, c, matrix, atlanticData)

        result = []
        # check which ones are visited by both pacific and atlantic
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if pacificData[r][c] == 1 and atlanticData[r][c] == 1:
                    result.append([r,c])
        return result

    def visit(self, r, c, matrix, data):
        # if marked already, ignore. ow mark it for appropriate ocean
        if data[r][c] == 1:
            return
        data[r][c] = 1
        R, C = len(matrix), len(matrix[0])
        for nr, nc in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
            if nr >= 0 and nr < R and nc >= 0 and nc < C:
                if matrix[nr][nc] >= matrix[r][c]:
                    self.visit(nr, nc, matrix, data)

   